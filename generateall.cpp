#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>


using namespace std;


//rating algorithm

double rater(string pw)
{
	int SIZE = pw.size();
	const int pw_size{SIZE};


    string basics{"1234567890qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM"};

    string specials{ "&$'|=!@#%^*()+[]{}?/:;<>~" } ;


    double basicnum{0};
    double specnum{0};
    double rating {0};


    for(int i{0} ; i < 62 ; i++)
    {

    	for(int j{0} ; j < pw_size ; j++)
    	{

    		if(basics[i] == pw[j]){
    			basicnum++;
				}
    	}
    }


    for(int i{0} ; i < 26 ; i++)
    {

    	for(int j{0} ; j < pw_size ; j++)
    	{

    		if(specials[i] == pw[j]){
    			specnum++;
				}
    	}
    }


	if(specnum == 0)
	specnum++;


    rating = basicnum / specnum ;

    return rating;}


int main()
{
	//making the rand func ready
	srand(time(NULL));

	int SIZE;

	string secki1 = "1234567890-=!@#$%^&*()_+qwertyuiop[]QWERTYUIOP{}asdfghjkl'ASDFGHJKL|zxcvbnm<>?/~ZXCVBNM";
	SIZE = secki1.size() ;
	const int size1{SIZE};


	string secki2 = "1234567890-=!@#$%^&*()_+qwertyuiop[]{}asdfghjkl'|zxcvbnm<>?/~";
	SIZE = secki2.size() ;
	const int size2{SIZE};

	string secki3 = "1234567890-=!@#$%^&*()_+[]QWERTYUIOP{}'ASDFGHJKL|<>?/~ZXCVBNM";
	SIZE = secki3.size() ;
	const int size3{SIZE};

	string secki4 = "1234567890qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM";
	SIZE = secki4.size() ;
	const int size4{SIZE};

	string secki5 =  "&$'|=!@#%^*()+[]{}?/:;<>~";
	SIZE = secki5.size() ;
	const int size5{SIZE};


	int ptimes{0}, ctimes{0}, tempctimes{0}, select{0}, randint{0};



	cout <<"GenerateAll\n\n0 - quit\n1 - all characters\n2 - except uppercase\n3 - except lowercase\n4 - only alphabet\n5 - only special\n----------\n";

	for(;;)
	{

		cout << "\n\nchoose :" ; cin >> select ;

		if(select == 0){
			break;
		}


		else if(select == 1)
		{	
			string filename;
			int flag{0};
			
			cout << "do you want to save it ? ( 1 / 0 ) :" ; cin >> flag ;
			
			if(flag == 1){
				cout << "give a file name : ";cin >> filename;
				}

			cout << "how many passwords do you want ? :" ; cin >> ptimes ;

			cout << "how many chars they will contain ? :" ; cin >> ctimes ;
			cout << endl << endl ;


			if(ptimes == 0)
				ptimes++;

			if(ctimes < 4)
				ctimes += 8;

			char password[ctimes]{'a'} ;
			
			
			//file things
			
			ofstream fout;
			fout.open(filename);

			for(int i{ptimes} ; i > 0; i--)
			{

				tempctimes = ctimes ;

				for(int j{tempctimes} ; j > 0 ; j--)
				{


					randint = (rand() % size1) - 1;

					password[ ctimes - j ] = secki1[randint] ;

				}

				string line{""};
				string ratepassword{""};

				for(int k{0} ; k < ctimes ; k++){
					cout << password[k] ;
					ratepassword += password[k];
					line += password[k];
							}

				cout << " ---> rating : no data\n" ;
				
				line += " ---> rating : no data\n" ;
				
				fout << line ;

			}
			fout.close();
			if(flag == 1)
			cout << "\n---\ncheck the file.\nall passwords saved.\n" ;


		}




		else if(select == 2)
		{
			string filename;
			int flag{0};
			
			cout << "do you want to save it ? ( 1 / 0 ) :" ; cin >> flag ;
			
			if(flag == 1){
				cout << "give a file name : ";cin >> filename;
				}	

			cout << "how many passwords do you want ? :" ; cin >> ptimes ;

			cout << "how many chars they will contain ? :" ; cin >> ctimes ;
			cout << endl << endl ;

			if(ptimes == 0)
				ptimes++;

			if(ctimes < 4)
				ctimes += 8;

			char password[ctimes]{'a'} ;
			
			
			//file things
			
			ofstream fout;
			fout.open(filename);

			for(int i{ptimes} ; i > 0; i--)
			{

				tempctimes = ctimes ;

				for(int j{tempctimes} ; j > 0 ; j--)
				{


					randint = (rand() % size2) - 1;

					password[ ctimes - j ] = secki2[randint] ;

				}
				string line{""};
				string ratepassword{""};

				for(int k{0} ; k < ctimes ; k++){
					cout << password[k] ;
					ratepassword += password[k];
					line += password[k];
							}

				cout << " ---> rating : no data\n" ;
				
				line += " ---> rating : no data\n" ;
				
				fout << line ;

			}
			fout.close();
			if(flag == 1)
			cout << "\n---\ncheck the file.\nall passwords saved.\n" ;


		}



		else if(select == 3)
		{
			string filename;
			int flag{0};
			
			cout << "do you want to save it ? ( 1 / 0 ) :" ; cin >> flag ;
			
			if(flag == 1){
				cout << "give a file name : ";cin >> filename;
				}
			cout << "how many passwords do you want ? :" ; cin >> ptimes ;

			cout << "how many chars they will contain ? :" ; cin >> ctimes ;
			cout << endl << endl ;

			if(ptimes == 0)
				ptimes++;

			if(ctimes < 4)
				ctimes += 8;

			char password[ctimes]{'a'} ;
			
			
			//file things
			
			ofstream fout;
			fout.open(filename);

			for(int i{ptimes} ; i > 0; i--)
			{

				tempctimes = ctimes ;

				for(int j{tempctimes} ; j > 0 ; j--)
				{


					randint = (rand() % size3) - 1;

					password[ ctimes - j ] = secki3[randint] ;

				}
				string line{""};
				string ratepassword{""};

				for(int k{0} ; k < ctimes ; k++){
					cout << password[k] ;
					ratepassword += password[k];
					line += password[k];
							}

				cout << " ---> rating : no data\n" ;
				
				line += " ---> rating : no data\n" ;
				
				fout << line ;

			}
			fout.close();
			if(flag == 1)
			cout << "\n---\ncheck the file.\nall passwords saved.\n" ;


		}



		else if(select == 4)
		{
			string filename;
			int flag{0};
			
			cout << "do you want to save it ? ( 1 / 0 ) :" ; cin >> flag ;
			
			if(flag == 1){
				cout << "give a file name : ";cin >> filename;
				}
			cout << "how many passwords do you want ? :" ; cin >> ptimes ;

			cout << "how many chars they will contain ? :" ; cin >> ctimes ;
			cout << endl << endl ;

			if(ptimes == 0)
				ptimes++;

			if(ctimes < 4)
				ctimes += 8;
				
				
			//file things
			
			ofstream fout;
			fout.open(filename);

			char password[ctimes]{'a'} ;

			for(int i{ptimes} ; i > 0; i--)
			{

				tempctimes = ctimes ;

				for(int j{tempctimes} ; j > 0 ; j--)
				{


					randint = (rand() % size4) - 1;

					password[ ctimes - j ] = secki4[randint] ;

				}

	string line{""};
				string ratepassword{""};

				for(int k{0} ; k < ctimes ; k++){
					cout << password[k] ;
					ratepassword += password[k];
					line += password[k];
							}

				cout << " ---> rating : no data\n" ;
				
				line += " ---> rating : no data\n" ;
				
				fout << line ;

			}
			
			fout.close();
			if(flag == 1)
			cout << "\n---\ncheck the file.\nall passwords saved.\n" ;


		}



		else if(select == 5)
		{
			string filename;
			int flag{0};
			
			cout << "do you want to save it ? ( 1 / 0 ) :" ; cin >> flag ;
			
			if(flag == 1){
				cout << "give a file name : ";cin >> filename;
				}
				
			cout << "how many passwords do you want ? :" ; cin >> ptimes ;

			cout << "how many chars they will contain ? :" ; cin >> ctimes ;
			cout << endl << endl ;

			if(ptimes == 0)
				ptimes++;

			if(ctimes < 4)
				ctimes += 8;

			char password[ctimes]{'a'} ;


			//file things
			
			ofstream fout;
			fout.open(filename);
			
			for(int i{ptimes} ; i > 0; i--)
			{

				tempctimes = ctimes ;

				for(int j{tempctimes} ; j > 0 ; j--)
				{


					randint = (rand() % size5) - 1;

					password[ ctimes - j ] = secki5[randint] ;

				}
				string line{""};
				string ratepassword{""};

				for(int k{0} ; k < ctimes ; k++){
					cout << password[k] ;
					ratepassword += password[k];
					line += password[k];
							}

				cout << " ---> rating : no data\n" ;
				
				line += " ---> rating : no data\n" ;
				
				fout << line ;

			}
			
			fout.close();
			if(flag == 1)
			cout << "\n---\ncheck the file.\nall passwords saved.\n" ;


		}




	}


	return 0 ;
}
