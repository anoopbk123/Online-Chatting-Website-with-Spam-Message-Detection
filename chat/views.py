from django.shortcuts import render
from chat.models import Chat
from friends.models import Friends
from user_reg.models import UserReg
from django.core.files.storage import FileSystemStorage

import datetime

from chat.models import Chat
# Create your views here.
import pandas as pd
from pandas import read_excel

from bs4 import BeautifulSoup
import re
import pickle

def html_tag(phrase):
    http_remove = re.sub(r"http\S+", "",phrase)
    html_remove = BeautifulSoup(http_remove, 'lxml').get_text()
    return html_remove

#remove words with numbers python: https://stackoverflow.com/a/18082370/4084039
#remove spacial character: https://stackoverflow.com/a/5843547/4084039
def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

stopwords= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"])

from tqdm import tqdm
from spam_message import settings
from sklearn.feature_extraction.text import TfidfVectorizer
def chat(request,abc):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    gm = Chat.objects.filter(friend_id=uid)
    context = {
        'name': objj,
        'chat':gm
    }

    if request.method == "POST":
        obj = Chat()
        uid = request.session["uid"]
        obj.friend_id= abc
        obj.user_id= uid
        obj.date = datetime.date.today()
        try:
            myfile = request.FILES["photo"]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            obj.photo = myfile.name
        except:
            pass

        obj.chat = request.POST.get('message')

        dspath=str(settings.BASE_DIR)+str(settings.STATIC_URL)+"spam.xls"
        trainData = read_excel(dspath)  # DATA FRAME -> COL, ROWS
        df2 = {'Label': 'ham', 'Content': obj.chat}
        trainData = trainData.append(df2, ignore_index=True)
        processed_review = []
        for i in trainData["Content"].values:
            sentance = html_tag(i)
            sentance = decontracted(sentance)
            sentance = re.sub("\S*\d\S*", "", sentance)
            sentance = re.sub('[^A-Za-z]+', ' ', sentance)
            sentance = " ".join(i.lower() for i in sentance.split() if i.lower() not in stopwords)
            processed_review.append(sentance)
        trainData["Cleantext"] = processed_review
        vectorizer = TfidfVectorizer(min_df=5,
                                     max_df=0.8,
                                     sublinear_tf=True,
                                     use_idf=True)
        train_vectors = vectorizer.fit_transform(trainData['Cleantext'])
        X_test1 = train_vectors[train_vectors.shape[0] - 1]

        mpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "model_dtc.sav"
        model = pickle.load(open(mpath, 'rb'))
        # y_score = model.predict(X_test)
        y_score = model.predict(X_test1)
        res = "This Message is :" + y_score[0]
        obj.status=y_score
        print(res)


        # obj.time = datetime.datetime.now().time()
        obj.time = datetime.datetime.now().strftime("%I:%M:%S")
        obj.save()


    return render(request,'chat/chat.html',context)


def chat_with_friends(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name

    print(uid)
    cd=UserReg.objects.filter(status='cyberbullying detected').values_list('user_id',flat=True)
    print(cd)
    # obj = Friends.objects.filter(request_status='accepted', f_user_id=uid)
    obj = Friends.objects.filter(request_status="accepted",user_id=uid)
    gm = Chat.objects.filter(friend_id=uid)
    chat_friend = {
            'chatfriend': obj,
             'name':objj,
             'chat':gm
        }
    return render(request,'chat/chat_with_friends.html',chat_friend)

def view_chat(request):
    uid = request.session["uid"]
    # print(uid)
    objj = UserReg.objects.filter(user_id=uid)  # name

    obj = Chat.objects.filter(friend_id=uid)
    gm = Chat.objects.filter(friend_id=uid)
    # gm = Chat.objects.filter(user_id=uid).exclude(friend_id=uid)
    print(gm)
    chatt = {
        'cha': obj,
        'name': objj,
        'chat':gm
    }

    return render(request,'chat/view_chat.html',chatt)