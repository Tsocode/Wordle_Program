{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red15\green112\blue1;\red5\green0\blue255;\red144\green1\blue18;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c0\c50196\c0;\cssrgb\c4314\c4314\c100000;\cssrgb\c63922\c8235\c8235;}
\margl1440\margr1440\vieww29200\viewh16220\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf0 \strokec4  modules \cf2 \strokec2 import\cf0 \strokec4  print_in_color\cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 ### DO NOT MODIFY ABOVE\cf0 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 \strokec4 def print_guess(\cf6 \strokec6 secret_word\cf0 \strokec4 , \cf6 \strokec6 guess\cf0 \strokec4 ):\cb1 \strokec4 \
\cb3 \strokec4   common \cf2 \strokec2 =\cf0 \strokec4  []\cb1 \strokec4 \
\
\cb3 \strokec4   res1 \cf2 \strokec2 =\cf0 \strokec4  \{vals : idxs \cf2 \strokec2 for\cf0 \strokec4  idxs, vals \cf2 \strokec2 in\cf0 \strokec4  enumerate(secret_word)\} \cf5 \strokec5 ##Making secret_word a dictionary\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf5 \strokec5 # print("The Dictionary after index keys : " + str(res1))\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf2 \strokec2 for\cf0 \strokec4  i \cf2 \strokec2 in\cf0 \strokec4  range(len(guess)):\cb1 \strokec4 \
\cb3 \strokec4     \cf2 \strokec2 if\cf0 \strokec4  guess[i] \cf2 \strokec2 in\cf0 \strokec4  secret_word:\cb1 \strokec4 \
\cb3 \strokec4       common.append(guess[i])\cb1 \strokec4 \
\cb3 \strokec4       \cf2 \strokec2 if\cf0 \strokec4  guess[i] \cf2 \strokec2 ==\cf0 \strokec4  secret_word[i]:\cb1 \strokec4 \
\cb3 \strokec4         print_in_color(guess[i],\cf7 \strokec7 "green"\cf0 \strokec4 )\cb1 \strokec4 \
\cb3 \strokec4       \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \strokec4 \
\cb3 \strokec4         print_in_color(guess[i],\cf7 \strokec7 "yellow"\cf0 \strokec4 )\cb1 \strokec4 \
\cb3 \strokec4     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \strokec4 \
\cb3 \strokec4       print_in_color(guess[i], \cf7 \strokec7 'red'\cf0 \strokec4 )\cb1 \strokec4 \
\cb3 \strokec4   \cf2 \strokec2 return\cf0 \strokec4  common\cb1 \strokec4 \
\
\cb3 \strokec4   \cf5 \strokec5 # for i in range(len(guess)):\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf5 \strokec5 #   if guess[i] in res1:\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf5 \strokec5 #     if i == res1[guess[i]]:\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf5 \strokec5 #       list1.append(print_in_color(guess[i],"green"))\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf5 \strokec5 #     else:\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf5 \strokec5 #       list1.append(print_in_color(guess[i],"yellow"))\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf5 \strokec5 #   else:\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf5 \strokec5 #     list1.append(print_in_color(guess[i],"red"))\cf0 \cb1 \strokec4 \
\
\cb3 \strokec4   \cf5 \strokec5 # return list1\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cb1 \strokec4 \
}