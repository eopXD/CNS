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
void eat () {
	for ( int i=0; i<5; i++ ) getchar();
} 
int main ()
{
	char s[1005]; eat(); gets(s);
	int n=strlen(s);
	for ( int i=0; i<26; i++ ) {
		for ( int j=0; j<n; j++ ) {
			if ( s[j]==' ' ) {
				putchar(' ');
				continue;
			}
			int tmp=s[j]+i;
			if ( isupper(s[j]) ) {
				if ( tmp>'Z' ) tmp-=26;
			}
			else {
				if ( tmp>'z' ) tmp-=26;
			}
			putchar(tmp);
		}
		puts("");
	}
	return 0;
}

