{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red15\green112\blue1;\red107\green0\blue1;\red144\green1\blue18;\red19\green118\blue70;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c0\c50196\c0;\cssrgb\c50196\c0\c0;\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c52549\c34510;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf0 \strokec4  get_guess_fn \cf2 \strokec2 import\cf0 \strokec4  get_guess                 \cf5 \strokec5 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  is_game_over_fn \cf2 \strokec2 import\cf0 \strokec4  is_game_over           \cf5 \strokec5 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  modules \cf2 \strokec2 import\cf0 \strokec4  print_in_color                 \cf5 \strokec5 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  print_guess_fn \cf2 \strokec2 import\cf0 \strokec4  print_guess             \cf5 \strokec5 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  is_valid_guess_fn \cf2 \strokec2 import\cf0 \strokec4  is_valid_guess       \cf5 \strokec5 #\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 ####################################################\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 \strokec4 secret_word \cf2 \strokec2 =\cf0 \strokec4  \cf6 \strokec6 str\cf0 \strokec4 (input(\cf7 \strokec7 "Enter the secret word: \cf6 \strokec6 \\n\cf7 \strokec7 "\cf0 \strokec4 ))\cb1 \strokec4 \
\cb3 \strokec4 required \cf2 \strokec2 =\cf0 \strokec4  []\cb1 \strokec4 \
\cb3 \strokec4 left \cf2 \strokec2 =\cf0 \strokec4  \cf8 \strokec8 6\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 while\cf0 \strokec4  \cf8 \strokec8 True\cf0 \strokec4 :\cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 \strokec4   g \cf2 \strokec2 =\cf0 \strokec4  get_guess(required)\cb1 \strokec4 \
\cb3 \strokec4   left \cf2 \strokec2 -=\cf0 \strokec4  \cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\cb3 \strokec4   \cf2 \strokec2 if\cf0 \strokec4 (is_game_over(secret_word,g,left)):\cb1 \strokec4 \
\cb3 \strokec4     \cf2 \strokec2 break\cf0 \cb1 \strokec4 \
\cb3 \strokec4   required \cf2 \strokec2 =\cf0 \strokec4  print_guess(secret_word, g)\cb1 \strokec4 \
\cb3 \strokec4   print()\cb1 \strokec4 \
\
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # def\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # def function_call(required_letters, secret_word, guess,tries_left):\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #   def get_guess(required_letters):\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     g = input("Enter your guess: \\n")\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     while is_valid_guess(g, required_letters) == False:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       message = "Your guess must contain all yellow and green letters from your previous guesses."\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       print(message)\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       g = input("Enter your guess: \\n")\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     if is_valid_guess(g, required_letters) == True:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       return g\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 #   def print_guess(secret_word, guess):\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     list1 = []\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     res1 = \{vals : idxs for idxs, vals in enumerate(secret_word)\} ##Making secret_word a dictionary\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     print("The Dictionary after index keys : " + str(res1))\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 #     for i in range(len(guess)):\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       if guess[i] in res1:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         if i == res1[guess[i]]:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #           list1.append(print_in_color(guess[i],"green"))\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         else:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #           list1.append(print_in_color(guess[i],"yellow"))\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       else:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         list1.append(print_in_color(guess[i],"red"))\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     return list1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 \strokec4     \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 #   def is_game_over(secret_word, guess, tries_left):\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     tries_left = 6\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     for letter in guess:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       if (guess == secret_word):\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         print("Correct! You got it in",tries_left," tries!")\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         tries_left -= 1\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     if tries_left == 0:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       print("Game over! The correct word is \{secret_word\}.")\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       return True\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     else:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #       return False\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     pass\cf0 \cb1 \strokec4 \
\
\
}