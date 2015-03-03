#!/usr/bin/python
import json, time, requests, urllib

while True:
    ticker = urllib.urlopen("https://beta.mining.bitcoin.cz/accounts/profile/json/121971-3978f22d8d96377e5f25b972190ac5f8")


    data =  json.load(ticker)
    c1 = data["username"]
    c2 = data["confirmed_reward"]
    c3 = data["hashrate"]
    c4 = data["unconfirmed_reward"]
    c5 = data["estimated_reward"]
    print c1
   # print "reward",c2
    print " Hasrate: ",c3
   # print " Unconfirmed Reward: ",c4
    print " Total Reward: ",c5

    print "#########",(time.strftime("%H:%M:%S")),"#########"

    time.sleep(360)