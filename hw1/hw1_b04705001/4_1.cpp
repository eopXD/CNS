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
void eat() {
	for ( int i=0; i<5; i++ ) getchar();
}
int main ()
{
	char s[1005]; eat(); gets(s);
	int n=strlen(s);
	vector<int> t;
	for ( int i=0, cnt=0, tmp=0; i<n; i++ ) {
		if ( s[i]!=' ' ) {
			tmp=tmp*10+s[i]-'0';
			cnt++;
		}
		else t.push_back(-64);
		
		if ( cnt==2 ) {
			t.push_back(tmp);
			cnt=tmp=0;
		}

	}
	for ( int i=0; i<SZ(t); i++ ) printf("%c",t[i]+'a'-1);
	puts("");

	return 0;
}

