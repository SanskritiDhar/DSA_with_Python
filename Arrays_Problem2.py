{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red245\green245\blue245;\red0\green0\blue0;\red101\green76\blue29;
\red144\green1\blue18;\red31\green99\blue128;\red19\green85\blue52;\red157\green0\blue210;\red15\green112\blue1;
}
{\*\expandedcolortbl;;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;\cssrgb\c47451\c36863\c14902;
\cssrgb\c63922\c8235\c8235;\cssrgb\c14510\c46275\c57647;\cssrgb\c6667\c40000\c26667;\cssrgb\c68627\c0\c85882;\cssrgb\c0\c50196\c0;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf0 \cb2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 num = \cf4 \strokec4 input\cf0 \strokec3 (\cf5 \strokec5 "Enter a number "\cf0 \strokec3 )\cb1 \
\cb2 num = \cf6 \strokec6 int\cf0 \strokec3 (num)\cb1 \
\
\cb2 n = num\cb1 \
\cb2 res = \cf7 \strokec7 0\cf0 \cb1 \strokec3 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb2 \strokec8 while\cf0 \strokec3  n>\cf7 \strokec7 0\cf0 \strokec3 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb2   \cf9 \strokec9 #taking last digit of the inital number \cf0 \cb1 \strokec3 \
\cb2   temp = n%\cf7 \strokec7 10\cf0 \cb1 \strokec3 \
\
\cb2   \cf9 \strokec9 # appending to resultant number\cf0 \cb1 \strokec3 \
\cb2   res = res*\cf7 \strokec7 10\cf0 \strokec3  + temp\cb1 \
\
\cb2   \cf9 \strokec9 #diving intial number by 10 , to get the next number\cf0 \cb1 \strokec3 \
\cb2   n = n//\cf7 \strokec7 10\cf0 \cb1 \strokec3 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb2 \strokec4 print\cf0 \strokec3 (\cf5 \strokec5 "reversed number is "\cf0 \strokec3 ,res)\cb1 \
}