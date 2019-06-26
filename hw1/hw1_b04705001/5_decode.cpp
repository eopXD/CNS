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
int transfer ( string str ) {
	int res=0;
	for ( int i=0; i<2; i++ ) {
		if ( isalpha(str[i]) ) res=res*16+str[i]-'a'+10;
		else res=res*16+str[i]-'0';
	}
	return res;
}
int main ()
{
	char s[1005]; gets(s);
	int n=strlen(s);
	vector<int> vec;
	string str;
	for ( int i=0; i<n; i++ ) {
		str+=s[i];
		if ( SZ(str)==2 ) {
			vec.push_back(transfer(str));
			str.clear();
		}
	}
	if ( !str.empty() ) {
		vec.push_back(transfer(str));
	}
	printf("%d\n",SZ(vec));
	for ( int i=0; i<SZ(vec); i++ ) putchar(vec[i]);
	puts("");
	return 0;
}

