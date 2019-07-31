
#ifdef __GNUC__ 
struct { int test_yoon_a ; } ;
#endif

enum enm1 {White=1, Black=4, Blue=8, Gray=7}; // test;
typedef enum {Kim, Lee, Park} Enm2;
enum enm3 {On, Off};

typedef struct node {
	enum enm1		a;
	int				b:2;
	unsigned int	c:4;
	char			*d;
	float			e[5];
	struct node		*next;
} Node;

typedef Node*	NodePtr;

union uni {
	Enm2	a;
	int		*c[7][8];
	Node	b;
};


void api1(int a, char b, float c, unsigned long int d, long double e);
enum enm3 api2(enum enm1 a, Enm2 b);
char* api3(char *a, char b[], char c[10]);
float api12 ( char c );

