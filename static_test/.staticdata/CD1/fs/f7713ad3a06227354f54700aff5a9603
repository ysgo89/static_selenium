/*	
 * 		GCC가 아닌경우에는 common C feature ( older than C99)만을
 * 		사용하도록 code가 만들어져 있다.
 *
 * 		그러므로 full testing purpose인 경우에는 gcc를 사용하고
 * 		그외 다른 compiler에 대해서는common C feature에 문제가 없는지를
 * 		확인하는 방식으로 사용하면 된다.
*/
#include	<stdio.h>
#include	<stdlib.h>

#include	"study_sample.h"

#ifdef __GNUC__ 
struct { int test_yoon_a ; } ;
#else
static struct { int test_yoon_a ; } ;
#endif

//char	*e1[] = {"", "White", "", "", "Black", "", "", "Gray", "Blue"};
//char	*e2[] = {"Kim", "Lee", "Park"};
//char	*e3[] = {"On", "Off"} ;
/*int test_stub0();*/
int test_stub1();

int global0;
float fl_var;

extern int sst_extern_A;
#define TEST_SUCCESS_VALUE  7


unsigned char testMe1();
unsigned char testMe2();
unsigned char timeOutFunc();

unsigned char testMe1()
{
	return timeOutFunc();
}

int charlesFunc(int a) {
	if(a == 1) {

	}
	if(a == 2) {
		return 2;
	}
	return -1;
}

unsigned char testMe2(int n)
{
	return n;
}

unsigned char timeOutFunc()
{
	unsigned char i = 0;

	for (i = 0; i <= 255; i++)
	{
		;
	}

	return i;
}


void timeout(){
	while(1){

	}
}

void stubFunc0 (sst_extern_A) {
	fl_var=sst_extern_A-10;
	if(test_stub0() == TEST_SUCCESS_VALUE){
		printf("SUCCESS\n");
	}
	else {
		printf("FAIL\n");
	}

}
/**/

int stubFunc1 () {
	int ret = test_stub1();
	switch(ret){
	case 1:
		printf("Return value is 1\n");
		break;
	case 2:
		printf("Return value is 2\n");
		break;
	case 3:
		printf("Return value is 3\n");
		break;
	default:
		return 1;
	}
	return 0;
}

int abc(int a){
	if(abc_1(a) > 0 ){
		printf("Return value is 1\n");
		if(stubFunc1 () != 0){
			printf("Return value is 3\n");
		}
	}
	else {
		printf("Return value is 2\n");
		if(stubFunc2 () != 0){
				printf("Return value is 4\n");
		}
	}
	timeout();
	return stubFunc2 ();
}
int abc_1(a){
	return 1;
}
int pTest(int * a){
	if(a > 0 ){
		printf("Return value is 1\n");
		if(stubFunc1 () != 0){
			printf("Return value is 3\n");
		}
	}
	else {
		printf("Return value is 2\n");
		if(stubFunc1 () != 0){
				printf("Return value is 4\n");
		}
	}
}

main( int argc, char* argv[] )
{
	int i = 0 ;

	char si='3';
	char sk='5';
	swap(&si,&sk,sizeof(int));
	printf("=========== int main( int argc, char* argv[] ): Input ===================\n");
	printf("argc:%d\n", argc);
	for (i=0; i < argc-1 ; i++ ) {
		printf("argv[%d]=\"%s\"\n", argv[i] );

	printf("=========== Input end ===================\n");
	}
	api12 ( 'a' ) ;
	printf("\n=========== int main( int argc, char* argv[] ): Output ===================\n");
	printf("no explicit return\n");
	printf("=========== Output end ===================\n");
}

void api1(int a, char b, float c, unsigned long int d, long double e)
{
	long double	ret;

	printf("=========== void api1(int a, char b, float c, unsigned long int d, long double e) Input ===================\n");
	printf("int a: %d\n", a);
	printf("char b: %c\n", b);
	printf("float c: %f\n", c);
	printf("unsigned long int d: %ul\n",d);
	printf("long double e: %Le\n", e);
	printf("=========== Input end ===================\n");


	ret = 1.0;
	
	while ( b != 0 ) {
		if ( a < 10 )
			ret -= a;
		else
			ret += a;
		if ( d > 50 )
			ret += d;
		b--;
	}
	
	if ( d == 0 && global0 == 0)
		ret *= d;
	
	if ( e != 0 && stubFunc1() != 1)
		ret *= e;
	else
		ret *= 2;
	

	printf("\n=========== enum enm3 api2(enum enm1 a, Enm2 b) Output ===================\n");
	printf("long double :  %Le\n", ret ) ;
	printf("=========== Output end ===================\n");
}

enum enm3 api2(enum enm1 a, Enm2 b)
{
	enum enm3	ret;
	
	printf("=========== enum enm3 api2(enum enm1 a, Enm2 b) Input ===================\n");
	printf("enum enm1 (1,4,7,8): %d\n", a );
	//printf("enum enm1 (White, Black, Gray, Blue): %s\n", e1[a]);
	printf("Enm2 (0,1,2): %d\n", b);
	/*printf("Enm2 (Kim, Lee, Park): %s\n", e2[b]);*/

	printf("=========== Input end ===================\n");

	ret=sst_extern_A;
	ret = (a - b) % 2;
	CSUT_LOG("ret");
	if((a != 1 && b != 2) || a < b){
		printf("MC/DC Success.\n");
	}

	if((a == 1) && (b == 4)){
		printf("MC/DC Success.\n");
	}

	printf("\n=========== enum enm3 api2(enum enm1 a, Enm2 b) Output ===================\n");
	printf("enum enm3 (0,1): %d\n", ret);
	//printf("enum enm3 (On, Off): %s\n", e3[ret]);
	printf("=========== Output end ===================\n");
	return ret;
}

Enm2 helper_Enm2(int b){
	Enm2 rt = b;
	return rt;
}


void exit_error(){
	exit(1);
}

void OutOfIndex_error(int i){
	char a[100];

	printf("%c\n", a[i]);
}


int loadFile(FILE* fp){
	char data[1024];
	int count;
	count = fread(data, sizeof(char), 1024, fp);
	if(count != 0){
		printf("FILE : %s", data);
		return 0;
	}
	else {
		return -1;
	}
}

FILE* helper(int a){
	FILE* fp = fopen("D:\\read.txt", "r");
	return fp;
}

int fibonacci_fail(int index){

	if(index == 0){
		return 0;
	}

	if(index == 1){
		return 1;
	}

	return fibonacci_fail(index - 1) + fibonacci_fail(index - 1);
}

int mcdcError(int a, int b, int c, int d){
 if(a==1){
  d=0;
 }
 else{
  if(a==2|| a==c){
   d=0;
  }
  if(b==0){
   if(a==6&&a>c){
    d=0;
   }
   else if(a>0 && a>c && c>0){
    d=0;
   }
   else if(a<0&& a<c && c<0){
    d=0;
   }
   else if(a<0 && a>c && c<0){
    d=0;
   }
   else if(a>0 && a>c && c<0){
    d=0;
   }
   else if(a>0&& a>c && c>0 && a>5){
    d=0;
   }
   else {
    d=0;
   }
  }
  else {
   if((a>0&&a>b)||c>0){
    d=0;
   }
   else if(a>0&&b>0){
    d=0;
   }
   else if((a<0&&a<b)||c<0){
    d=0;
   }
   else if(a<0&&b<0){
    d=0;
   }
   else if(a<0&&c<0){
    d=0;
   }
   else if(a>0&&c>0){
    d=0;
   }
   else if(a==0&&c==0){
    d=0;
   }
   else if(a>0&&c==0){
    d=0;
   }
   else if((a>0||b>0)&&c==0){
    d=0;
   }
   else if(((a>0&&b>0)||c!=0)&&(a>3||b>3)){
    d=0;
   }
   else if(((a>0||b>0)||c==0)&&a>b){
    d=0;
   }
   else if((a<0&&b>0) && (a<c&&c>0)){
    d=0;
   }
   else if(a<0&&c==0){
    d=0;
   }
   else{
    d=0;
   }
  }
 }
 return 0;
}


