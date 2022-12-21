{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red5\green0\blue255;\red19\green118\blue70;\red144\green1\blue18;\red107\green0\blue1;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c4314\c4314\c100000;\cssrgb\c3529\c52549\c34510;\cssrgb\c63922\c8235\c8235;\cssrgb\c50196\c0\c0;}
\margl1440\margr1440\vieww29200\viewh16220\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf0 \strokec4  is_valid_guess_fn \cf2 \strokec2 import\cf0 \strokec4  is_valid_guess\cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 \strokec4 def get_guess(\cf5 \strokec5 required_letters\cf0 \strokec4 ):\cb1 \strokec4 \
\cb3 \strokec4   \cf2 \strokec2 while\cf0 \strokec4  \cf6 \strokec6 True\cf0 \strokec4 :\cb1 \strokec4 \
\cb3 \strokec4     g \cf2 \strokec2 =\cf0 \strokec4  input(\cf7 \strokec7 "Enter your guess: \cf8 \strokec8 \\n\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \strokec4 \
\cb3 \strokec4     valid \cf2 \strokec2 =\cf0 \strokec4  is_valid_guess(g, required_letters)\cb1 \strokec4 \
\cb3 \strokec4     \cf2 \strokec2 if\cf0 \strokec4  (\cf2 \strokec2 not\cf0 \strokec4  valid):\cb1 \strokec4 \
\cb3 \strokec4       message \cf2 \strokec2 =\cf0 \strokec4  \cf7 \strokec7 "Your guess must contain all yellow and green letters from your previous guesses."\cf0 \cb1 \strokec4 \
\cb3 \strokec4       print(message)\cb1 \strokec4 \
\cb3 \strokec4     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \strokec4 \
\cb3 \strokec4       \cf2 \strokec2 return\cf0 \strokec4  g\cb1 \strokec4 \
}