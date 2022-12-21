{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue254;\red0\green0\blue0;\red5\green0\blue255;
\red0\green0\blue255;\red144\green1\blue18;\red19\green118\blue70;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;\cssrgb\c4314\c4314\c100000;
\cssrgb\c0\c0\c100000;\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c52549\c34510;}
\margl1440\margr1440\vieww29200\viewh16220\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs30 \cf0 \cb2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 def is_game_over(\cf4 \strokec4 secret_word\cf0 \strokec3 , \cf4 \strokec4 guess\cf0 \strokec3 , \cf4 \strokec4 tries_left\cf0 \strokec3 ):\cb1 \strokec3 \
\cb2 \strokec3   \cf5 \strokec5 if\cf0 \strokec3  secret_word \cf5 \strokec5 ==\cf0 \strokec3  guess:\cb1 \strokec3 \
\cb2 \strokec3     print(\cf6 \strokec6 'Correct! You got it in'\cf0 \strokec3 , \cf7 \strokec7 6\cf5 \strokec5 -\cf0 \strokec3 tries_left, \cf6 \strokec6 'tries!'\cf0 \strokec3 )\cb1 \strokec3 \
\cb2 \strokec3     \cf5 \strokec5 return\cf0 \strokec3  \cf7 \strokec7 True\cf0 \cb1 \strokec3 \
\cb2 \strokec3   \cf5 \strokec5 if\cf0 \strokec3  tries_left \cf5 \strokec5 ==\cf0 \strokec3  \cf7 \strokec7 0\cf0 \strokec3 :\cb1 \strokec3 \
\cb2 \strokec3     print(\cf6 \strokec6 'Game over! The correct word is'\cf0 \strokec3 ,secret_word\cf5 \strokec5 +\cf6 \strokec6 '.'\cf0 \strokec3 )\cb1 \strokec3 \
\cb2 \strokec3     \cf5 \strokec5 return\cf0 \strokec3  \cf7 \strokec7 True\cf0 \cb1 \strokec3 \
\cb2 \strokec3   \cf5 \strokec5 return\cf0 \strokec3  \cf7 \strokec7 False\cf0 \cb1 \strokec3 \
}