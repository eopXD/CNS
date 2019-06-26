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
int guess_length ( int len ) {
	vector<vector<int> > vec;
	vector<int> tmp;
	for ( int i=0; i<SZ(ciphertext); i++ ) {
		if ( SZ(tmp)==len ) {
			vec.push_back(tmp);
			tmp.clear();
		}
		tmp.push_back(ciphertext[i]);
	}
	vec.push_back(tmp);

	for ( int i=0; i+1<SZ(vec); i++ ) {
		for ( int j=0; j<SZ(vec[i]); j++ ) {
			printf("%.3d ",vec[i][j]);
		}
		puts("");
		for ( int j=0; j<SZ(vec[i+1]); j++ ) {
			printf("%.3d ",vec[i+1][j]);
		}
		puts("");
		for ( int j=0; j<SZ(vec[i])&&j<SZ(vec[i+1]); j++ ) {
			int power_ranger=vec[i][j]^vec[i+1][j];	
			if ( isalpha(power_ranger) ) printf("__%c ",power_ranger);
			else printf("%.3d ",power_ranger);
			if ( power_ranger>127 ) return 0;
		}

		puts("");
		puts("==============");
	}
	return 1;
}
int main ()
{
	load_otp();
	
	freopen("output.txt","w",stdout);
/*	for ( int i=1; i<=50; i++ ) {
		if ( guess_length(i) ) {
			printf("%d: OK!!!!!\n",i);
		}
	}*/
	guess_length(26);
	return 0;
}

