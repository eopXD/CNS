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
	char t[1005]; eat(); gets(t);
	int x=s[0]-t[0];
	getchar();
	char u[1005]; eat(); gets(u);
	int n=strlen(u);
	for ( int i=0; i<n; i++ ) {
		if ( u[i]!=' ' ) {
			int tmp=u[i]+x;
			if ( isupper(u[i]) ) {
				if ( tmp>'Z' ) putchar(tmp-26);
				if ( tmp<'A' ) putchar(tmp+26);
				else putchar(tmp);
			}
			else {
				if ( tmp>'z' ) putchar(tmp-26);
				else if ( tmp<'a' ) putchar((char)(tmp+26));
				else putchar(tmp);
			}
		}
		else putchar(' ');
	}
	puts("");
	return 0;
}

