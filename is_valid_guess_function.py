{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue254;\red0\green0\blue0;\red5\green0\blue255;
\red0\green0\blue255;\red19\green118\blue70;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;\cssrgb\c4314\c4314\c100000;
\cssrgb\c0\c0\c100000;\cssrgb\c3529\c52549\c34510;}
\margl1440\margr1440\vieww29200\viewh16220\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs30 \cf0 \cb2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 def is_valid_guess(\cf4 \strokec4 guess\cf0 \strokec3 , \cf4 \strokec4 required_letters\cf0 \strokec3 ):\cb1 \
\cb2   \cf5 \strokec5 for\cf0 \strokec3  letter \cf5 \strokec5 in\cf0 \strokec3  required_letters:\cb1 \
\cb2     \cf5 \strokec5 if\cf0 \strokec3  letter \cf5 \strokec5 not\cf0 \strokec3  \cf5 \strokec5 in\cf0 \strokec3  guess:\cb1 \
\cb2       \cf5 \strokec5 return\cf0 \strokec3  \cf6 \strokec6 False\cf0 \cb1 \strokec3 \
\cb2   \cf5 \strokec5 return\cf0 \strokec3  \cf6 \strokec6 True\cf0 \cb1 \strokec3 \
\
}