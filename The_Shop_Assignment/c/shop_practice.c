
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Function DEclerations
void open_no_money();
void open_no_bread();
const char* getfield(char*, int );
void my_menu();
void no_money();
void customer();
void much_bread(int,char [] ,int );
void customer_csv();
//Global Variables
float customer_budget;
char customer_name[100];
float shop_budget = 1000.3;
float sum=0.0;   
//My Functions

void open_no_money()
{
    FILE *fptr;   
    char c;
    // Open file 
    fptr = fopen("customer_not_enough_money.csv", "r"); 
    if (fptr == NULL) 
    { 
        printf("Cannot open file \n"); 
        exit(0); 
    } 
  
    // Read contents from file 
    c = fgetc(fptr); 
    while (c != EOF) 
    { 
        printf ("%c", c); 
        c = fgetc(fptr); 
    } 
  
    fclose(fptr); 
    printf("\n");
}

void open_no_bread()
{
    FILE *fptr;   
    char c;
    // Open file 
    fptr = fopen("customer_too_much_bread.csv", "r"); 
    if (fptr == NULL) 
    { 
        printf("Cannot open file \n"); 
        exit(0); 
    } 
  
    // Read contents from file 
    c = fgetc(fptr); 
    while (c != EOF) 
    { 
        printf ("%c", c); 
        c = fgetc(fptr); 
    } 
  
    fclose(fptr);
    printf("\n"); 
}


void customer()
{
    FILE *myfile = fopen("customer.csv","w");
    printf("Enter Customer name : ");
    scanf("%s",customer_name);    
    printf("Enter Customer total budget : ");
    scanf("%f",&customer_budget);
    fprintf (myfile, "%s",customer_name);
    fprintf (myfile, "%f\n",customer_budget);
}

void customer_csv()
{

    FILE *fptr;   
    char c;
    // Open file 
    fptr = fopen("customer.csv", "r"); 
    if (fptr == NULL) 
    { 
        printf("Cannot open file \n"); 
        exit(0); 
    } 
  
    // Read contents from file 
    c = fgetc(fptr); 
    while (c != EOF) 
    { 
        printf ("%c", c); 
        c = fgetc(fptr); 
    } 
  
    fclose(fptr); 
    printf("\n");
}

void much_bread(int param1,char param2[],int param3)
{

printf("Fail\n");
printf("Not Enough Customer Money\n");
printf("Totaal of 0 deducted from ");

printf("%s",customer_name);
printf(" money");

printf("\ntotal of 0 added in the shop \n");
printf("Shop has ");
printf("%f",shop_budget);
printf(" in cash\n");

}

void no_money()
{

printf("Fail\n");
printf("Not Enough Money\n");
printf("\nTotal of 0 will be deducted from customer budget\n");
printf("\ntotal of 0 added in the shop \n");
printf("Shop has ");
printf("%f",shop_budget);
printf(" in cash\n");

}

void live_mode()
{
printf("\n---------------------------------------------------------------\n");
int my_choice;
int coke=0,bread=0,speg=0,sauce=0,bag=0;
  printf("Live mode loaded\n");
    			     printf("1 Coke can\n");
    			        printf("2 Bread\n");
    			            printf("3 Spaghetti\n");
    		                printf("4 Tomato Sauce\n");
    		             printf("5 Big Bags\n");
    		            printf("6 Back to menu\n");
                        printf("What do you want to purchase:e.g type 1,2,3,4 : ");
               scanf("%d",&my_choice);
               switch(my_choice)
               {
               case 1:
               	printf("Enter the Ammount of Coke can you want to purchase : ");
               	scanf("%d",&coke);
               	if(coke > 100)
               	{
               	char coke_can[20] = "COke Can";
               	int coke_1=100;
               	printf("Sorry!Shop has only 100 coke cans\n");
               	much_bread(coke_1,coke_can,coke);
               	}
               	else
               	{
               	printf("Total coke can ammount for you to pay : ");
               	coke = coke * 1.1 ;
               	sum = sum + coke;
               	printf("%d\n",coke);
        
               	}
               	break;
               case 2:
               	printf("Enter the Ammount of Bread you want to purchase : ");
               	scanf("%d",&bread);
               	if(bread > 30)
               	{
               	char our_bread[20] = "Bread";
               	int bread_1=30;
               	printf("Sorry!Shop has only 30 breads\n");
               	much_bread(bread_1,our_bread,bread);
               	}
               	else
               	{
               	printf("Total  breads ammount for you to pay : ");
               	bread = bread * 0.7 ;
               	sum = sum + bread ;
               	printf("%d\n",bread);
        
               	}
               	break;
               case 3:
               	printf("Enter the Ammount of speghitti you want to purchase : ");
               	scanf("%d",&speg);
               	if(speg > 100)
               	{
               	char our_speg[20] = "Speghitti";
               	int speg_1=100;
               	printf("Sorry!Shop has only 100 speghitti\n");
               	much_bread(speg_1,our_speg,speg);
               	}
               	else
               	{
               	printf("Total  speghitti ammount for you to pay : ");
               	speg = speg * 1.2 ;
               	sum = sum + speg;
               	printf("%d\n",speg);
        
               	}
               	break;
               case 4:
               	printf("Enter the Ammount of Tomato Sauce  you want to purchase : ");
               	scanf("%d",&sauce);
               	if(sauce > 100)
               	{
                       char our_sauce[20] = "Tomato Sauce";
               	int sauce_1=100;
               	printf("Sorry!Shop has only 100 Tomato sauce\n");
               	much_bread(sauce_1,our_sauce,sauce);
               	
               	}
               	else
               	{
               	printf("Total  speghitti ammount for you to pay : ");
               	sauce = sauce * 1.8 ;
               	sum = sum + sauce;
               	printf("%d\n",sauce);
        
               	}
               	break;
               case 5:
               	printf("Enter the Ammount of Big Bags  you want to purchase : ");
               	scanf("%d",&bag);
               	if(bag > 4)
               	{
               
               	char our_bag[20] = "Big Bag";
               	int bag_1=100;
               	printf("Sorry!Shop has only 4 Big Bags\n");
               	much_bread(bag_1,our_bag,bag);
               	
               	}
               	else
               	{
               	printf("Total Big Bags ammount for you to pay : ");
               	bag = bag * 2.5 ;
               	sum = sum + bag;
               	printf("%d\n",bag);
        
               	}
               	break;
               case 6:
                      my_menu();
               default:
                       printf("Invalid Input \n");
               	}
               	
               	live_mode();
               	
}

void my_menu()
{
int choice;
char our_order[20] = "No order yet\n";
int order_1=0;
int order_2=0;
 printf("\n---------------------------------------------------------------\n");
    printf("Welcome to the shop\n");
        printf("1 For live mode\n");
            printf("2 Customer_to_much_bread.csv\n");
                printf("3 Customer.csv\n");
                    printf("4 Customer not enough money.csv\n");
                      printf("5 To pay bill\n");
                       printf("6 To pay bill\n");
                        printf("Choose your customer file or live mode:e.g type 1,2,3,4 : ");
               scanf("%d",&choice);
               
               switch(choice)
               {
               case 1:
                      printf("\n---------------------------------------------------------------\n");
                      customer();

                      live_mode();  
                      break;	
               case 2:
                      open_no_bread();
                      break;
               case 3:
                      customer_csv();
                      break;
               case 4:
                      open_no_money();
                      break;
               case 5:
                      if( sum > customer_budget )
                      {
                      no_money();
                      }
                      else
                      {
                       printf("Success!\n");
                       printf("%s",customer_name);
			printf(" Budget is ");
			printf("%f",customer_budget);
                       printf("\n John Has Enough money \n");
                       printf("Total of ");
                       printf("%f",sum);
                       printf(" Will be deducted from ");
                       printf("%s",customer_name);
                       customer_budget = customer_budget - sum;
                       printf("%s",customer_name);
                       printf(" ");
                       printf("%f",customer_budget);
                       shop_budget = shop_budget + sum;
                       printf("Shop budget changes to : ");
                       printf("%f",sum);
                      }
                      break;
                case 6:
                      exit(0);
                      break;
               default:
               	printf("invalid input \n ");
               	break;
               }
               my_menu();

}
const char* getfield(char* line, int num)
{
    const char* tok;

    for (tok = strtok(line, ";");
            tok && *tok;
            tok = strtok(line, ";\n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}

int main()
{

    FILE* stream = fopen("stock.csv", "r");
    float customer_bill =  0;
    char line[50];
    printf("---------------------------------------------------------------\n");
    while (fgets(line, 50, stream))
    {   
        char* tmp = strdup(line);
        printf("%s\n", getfield(tmp, 3));
        // NOTE strtok clobbers tmp
        free(tmp);
    }
    my_menu();
      return 0;    
}



