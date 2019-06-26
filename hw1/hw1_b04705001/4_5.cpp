//#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
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
char s[100],t[100],u[100];
int n;
vector<char> grid[100];
int gridn,gridm;
bool good_first () {
	for ( int i=0; i<gridn; i++ ) 
		if ( grid[i][0]!=t[i] ) 
			return 0;	
	return 1;
}
bool guess_length ( int x ) {
	for ( int i=0; i<100; i++ ) grid[i].clear();
	gridn=0;
	for ( int i=0; i<n; i++ ) {
		if ( SZ(grid[gridn])==x ) gridn++;
		grid[gridn].push_back(s[i]);
	}
	gridn++;
	if ( good_first() ) return 1;
	else return 0;
}
void eat () {
	for ( int i=0; i<5; i++ ) getchar();
}
void print_grid () {
	for ( int i=0; i<gridn; i++ ) {
		printf("%.2d:%.2d: ",i,SZ(grid[i]));
		for ( int j=0; j<SZ(grid[i]); j++ ) 
			printf("%c%c",grid[i][j],j==SZ(grid[i])-1?'\n':' ');
	}
	puts("=======");
}
void spin_grid () {
	vector<char> tmp[100];
	for ( int j=0; j<gridm; j++ ) {
		for ( int i=0; i<gridn && j<SZ(grid[i]); i++ ) {
			tmp[j].push_back(grid[i][j]);
		}
	}
	for ( int i=0; i<100; i++ ) grid[i].clear();
	swap(gridn,gridm);
	for ( int i=0; i<gridn; i++ ) 
		for ( int j=0; j<SZ(tmp[i]); j++ ) 
			grid[i].push_back(tmp[i][j]);
}
vector<int> seq[100000];
vector<int> tmp_seq;
int seqn;
void push_seq () {
	for ( int i=0; i<SZ(tmp_seq); i++ ) 
		seq[seqn].push_back(tmp_seq[i]);
	seqn++;
}
int used[100];
bool fit ( int grid_n, int at_t ) {
	for ( int i=0; i<SZ(grid[grid_n]); i++ ) 
		if ( grid[grid_n][i]!=t[at_t+i] ) 
			return 0;
	return 1;
}
void gogo_power_ranger ( int now, int at_t ) {
	if ( now==gridn ) {
		push_seq();
		return ;
	}
//	printf("%d %dXDD\n",now,at_t);
//	puts("still in power~~QAQ");
	for ( int i=0; i<gridn; i++ ) {
		if ( used[i] ) continue;
		if ( fit(i,at_t) ) {
			used[i]=1;
			tmp_seq.push_back(i);
			gogo_power_ranger(now+1,at_t+SZ(grid[i]));
			tmp_seq.pop_back  ();
			used[i]=0;
		}
	}
//	puts("DOOOOM");	
}
void print_seq () {
	for ( int i=0; i<seqn; i++ ) 
		for ( int j=0; j<SZ(seq[i]); j++ ) 
			printf("%d%c",seq[i][j],j==SZ(seq[i])-1?'\n':' ');
}
struct P {
	int id;
	vector<char> s;
};
bool cmp ( P a, P b ) { return a.id<b.id; }
vector<P> cipher;
void print_cipher () {
	for ( int i=0; i<SZ(cipher); i++ ) {
		printf("%.2d: ",SZ(cipher[i].s)); 

		for ( int j=0; j<SZ(cipher[i].s); j++ ) 
			printf("%c%c",cipher[i].s[j],j==SZ(cipher[i].s)-1?'\n':' ');
	}
	puts("=======");
}

void spin_cipher () {
	vector<P> tmp;
//	printf("%d %d\n",gridn,gridm);
	for ( int j=0; j<gridm; j++ ) {
		P ttmp;
		for ( int i=0; i<gridn && j<SZ(cipher[i].s); i++ ) 
			ttmp.s.push_back(cipher[i].s[j]);	
		tmp.push_back(ttmp);
	}	
	cipher.clear();
	swap(gridn,gridm);
	for ( int i=0; i<gridn; i++ )
		cipher.push_back(tmp[i]);
}
void decode () {
	for ( int i=0; i<SZ(cipher); i++ )
		for ( int j=0; j<SZ(cipher[i].s); j++ )
			putchar(cipher[i].s[j]);
	puts("");
}
int main ()
{
	eat(); gets(s); 
	eat(); gets(t); 
	getchar();
	eat(); gets(u);
	n=strlen(s);
	freopen("output.txt","w",stdout);
	for ( int zzz=1; zzz<=n-5; zzz++ ) {
		if ( guess_length(zzz) ) {
			gridm=zzz;
//			print_grid();
			spin_grid();
//			print_grid();
			for ( int i=0; i<100000; i++ ) seq[i].clear();
			seqn=0;
			gogo_power_ranger(0,0);

//			print_seq();

			for ( int i=0; i<seqn; i++ ) {
				int cnt=0;
				cipher.clear();
				for ( int j=0; j<SZ(seq[i]); j++ ) {
					P tmp;
					tmp.id=seq[i][j];
					for ( int k=0; k<SZ(grid[seq[i][j]]); k++ ) {
						if ( isupper(u[cnt]) ) tolower(u[cnt]);
						tmp.s.push_back(u[cnt++]);
					}
					cipher.push_back(tmp);
				}
//				print_cipher();
				sort(cipher.begin(),cipher.end(),cmp);
//				print_cipher();
				spin_cipher();
//				print_cipher();
				decode();
				swap(gridn,gridm);;
			}
//			break;
			for ( int i=0; i<10; i++ ) printf("%d",zzz);
			puts("");
		}
	}
	return 0;
}

