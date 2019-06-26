//#include <bits/stdc++.h>
#include <cstdio>
#include <cmath>
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
int Euler(int n){
	int ans=n;
	for(int i=2;i*i<=n;i++){
		if(n%i==0){
			ans=ans/i*(i-1);
			while(n%i==0)n/=i;
		}
	}
	if(n>1)ans=ans/n*(n-1);
	return ans;
}
int pow_mod ( int a,int b ) { //條件:gcd(a,b)=1
	int mod=b,tmd=a,ans=1;
	for(b=Euler(b)-1;b;b>>=1){
		if ( b&1 ) ans=ans*tmd%mod;
		tmd=tmd*tmd%mod;
	}
	return ans;
}
bool is_prime ( int x ) {
	for ( int i=2; i<=sqrt(x); i++ ) 
		if ( x%i==0 ) return 0;
	return 1;
}
void eat () {
	for ( int i=0; i<5; i++ ) getchar();
}
int main ()
{
	char s[1005]; eat(); gets(s);
	char t[1005]; eat(); gets(t);
	int n=strlen(s);
	int a=-1, b=-1;
	int ni;
	for ( int i=0; i<n; i++ ) {
		for ( int j=i+1; j<n; j++ ) {
//			printf("%d %d\n",i,j);
			int q=s[i]-'a'; int w=t[i]-'a';
			int e=s[j]-'a'; int r=t[j]-'a';
			if ( s[i]<=s[j] || s[j]=='a' || t[i]<=t[j] ) continue;
			if ( s[i]==' ' || s[j]==' ' ) continue;
			int tmp=q-e, tmp2=w-r;
			if ( !is_prime(tmp) ) continue;
			if ( s[i]<=t[i] || s[j]<=t[j] ) continue;
			if ( isupper(s[i]) || isupper(t[i]) || isupper(s[j]) || isupper(t[j]) ) continue;
			printf("%c %c %c %c\n",s[i],s[j],t[i],t[j]);
			while ( tmp2<0 ) tmp2+=26;

			ni=pow_mod(tmp,26);
//			printf("%d\n",ni);
			a=(tmp2*ni)%26;
//			printf("%d %d\n",q*r,w*e);	
			tmp2=q*r-w*e;
//			printf("%d\n",tmp2);
			b=(tmp2*ni)%26;
			break;
		}
		if ( a!=-1 ) break;
	}
/*	printf("\n%d %d\n",a,b);
	for ( int i=0; i<n; i++ ) {
		if ( s[i]==' ' ) putchar(' ');
		else {
			int tmp=((s[i]-'a')*a+b)%26;
			while ( tmp<0 ) tmp+=26;
			putchar(tmp+'a');
		}
	}
	puts("");*/
	getchar();
	char u[1005]; eat(); gets(u);
	n=strlen(u);
	ni=pow_mod(a,26);
	for ( int i=0; i<n; i++ ) {
//		printf("\n%c: ",u[i]);
		if ( u[i]==' ' ) { putchar(' '); continue; }
		int tmp=u[i]-'a';
		if ( isupper(u[i]) ) tmp=tolower(u[i])-'a';
		int tmp2=(ni*(tmp-b))%26;
		while ( tmp2<0 ) tmp2+=26;
		if ( isupper(u[i]) ) putchar(toupper(tmp2+'a'));
		else putchar(tmp2+'a');
	}
	puts("");
	return 0;
}

