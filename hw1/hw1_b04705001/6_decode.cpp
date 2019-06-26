//#include <bits/stdc++.h>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <climits>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#define SZ(x) (int)((x).size())
#define PII pair<int,int>
#define PB push_back
#define MP make_pair
using namespace std;
typedef long long LL;
int alpha_to_digit ( string str ) {
	int res=0;
	for ( int i=0; i<SZ(str); i++ ) {
		if ( isalpha(str[i]) ) res=res*16+str[i]-'a'+10;
		else res=res*16+str[i]-'0';
	}
	return res;
}
vector<int> ciphertext;
void load_otp () {
	freopen("otp.txt","r",stdin);
	char c;
	string str;
	while( (c=getchar())!=EOF ) {
		str+=c;
		if ( SZ(str)==2) {
			ciphertext.push_back(alpha_to_digit(str));
			str.clear();
		}
	}
}
int key_space[13]={137,77,233,47,124,194,223,176,244,91,255,87,180};
vector<int> key;
void gen_key () {
	for ( int i=0; i<13; i++ ) key.push_back(key_space[i]^' ');
}
vector<int> plain;
void decode () {
	int at=0;
	for ( int i=0; i<SZ(ciphertext); i++ ) {
		if ( at==SZ(key) ) at=0;
		int tmp=ciphertext[i]^key[at++];
		plain.push_back(tmp);
	}
	puts("");
	for ( int i=0; i<SZ(plain); i++ ) printf("%c",plain[i]);
	puts("");
}
int main ()
{
	load_otp();
//	freopen("plain.txt","w",stdout);
	gen_key();
	decode();
	return 0;
}

