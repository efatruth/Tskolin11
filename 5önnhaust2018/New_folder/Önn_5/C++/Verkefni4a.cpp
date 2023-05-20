#include <iostream>
#include <sstream>
#include <iomanip> //Nota iomanip til �ess a� f� setprecision.
#include <math.h> //Nota math.h fyrir ceil.
using namespace std;

class FlightBooking {
public:
	FlightBooking(int id, int capacity, int reserved);
	void printStatus();
	bool reserveSeats(int flightID, int number_of_seats);
	bool cancelReservations(int flightID, int number_of_seats);
private:
	int id;
	int capacity;
	int reserved;
};

void FlightBooking::printStatus()
{

	float procentage = (float(reserved) / float(capacity)) * 100; //Breyti b��i breytunum � float svo a� �g get reikna� pr�sentuna.
	cout << "\n" << "Flight " << id << " : " << reserved << "/" << capacity << " (" << fixed << setprecision(0) << procentage << "%)  seats reserved" << "\n\n";
	//Kalla �essa runu til �ess a� prenta �t allt sem �g �arf + l�ka pr�sentut�luna me� �v� a� nota "setprecision(0)" til a� round-a t�luna
	//svo a� pr�sentan ver�ur ekki me� neina aukastafi, og "fixed" til �ess a� f� 'fixed floating-point notation'.
}
FlightBooking::FlightBooking(int id, int capacity, int reserved)
{
	FlightBooking::id = id;
	FlightBooking::capacity = capacity;
	FlightBooking::reserved = reserved;
}

bool FlightBooking::reserveSeats(int flightID, int number_of_seats)
{
	float newReserved = float(reserved) + float(number_of_seats); //Geri n�ja breytu me� newReserved til �ess a� sleppa �v� a� sko�a tvisvar hvort �a� s� pl�ss fyrir fleiri reservations.
	float procentage = ceil((float(newReserved) / float(capacity)) * 100);
	//�essi breyta er notu� fyrir ne�an til a� sko�a hvort �a� s� h�gt a� b�ta vi� auka reservations.
	//�g nota l�ka "ceil" til a� round-a ni�ur svo a� �a� ver�ur ekki 15.x pr�sent. (�g m�tti r��a a� nota floor e�a ceiling.)
	if (procentage <= 105)
	{
		FlightBooking::reserved += number_of_seats; //B�ti vi� reservations.
		return true;
	}
	else
		return false;
}

bool FlightBooking::cancelReservations(int flightID, int number_of_seats)
{
	int checkReserved = (reserved - number_of_seats); //Nota �essa breytu fyrir ne�an til �ess a� sko�a hvort �g er me� n�g af resrvations til �ess a� fjarl�ga � burtu.
	if (checkReserved >= 0)
	{
		FlightBooking::reserved -= number_of_seats; //Fjarl�gi reservations ef �a� eru ekki undir 0.
		return true;
	}
	else if (checkReserved < 0) //Ef s�tin eru negat�f eftir �a� er b�i� a� fjarl�ga fr�, vistast s�tin sem 0.
	{
		FlightBooking::reserved = 0;
		return true;
	}
	else //Ef eitthva� fer �rskei�is.
		return false;
}


int main() {
	string failedString = "\n Cannot perform this operation \n\n";
	string fEdit; // Strengur sem heldur � user-input. fEdit stendur fyrir "Flight Edit"
	bool loop = true;
	int reserved = 0,
		capacity = 0;
	cout << "Provide flight capacity: ";
	cin >> capacity;
	cout << "Provide number of reserved seats: ";
	cin >> reserved;

	FlightBooking booking(1, capacity, reserved);

	booking.printStatus();

	while (loop == true)
	{
		cout << "----------------------------------- \n";
		cout << "Welcome User. \n";
		cout << "You have 3 procedures available: \n";
		cout << "add [ID] [integer] \n";
		cout << "cancel [ID] [integer] \n";
		cout << "quit" << "\n \n";
		cout << "An example procedure would be: \n";
		cout << "add 1 4 \n";
		cout << "or \n";
		cout << "cancel 3 20 \n";
		cout << "----------------------------------- \n";

		cout << "Choose Procedure: ";
		getline(cin, fEdit);

		int id; // Velja flight number ID
		int cap; // Hversu marga � a� taka e�a setja inn.
		string procedure; // Taka fram hva� procedure �g nota.
		stringstream procedureString; // Setja svo � string stream.
		procedureString << fEdit;
		procedureString >> procedure >> id >> cap;
		if (procedure == "add") // Fyrir a� b�ta vi�
		{
			if (booking.reserveSeats(id, cap) == true) // �essi if-setning keyrir falli� � rauninni, �annig a� �g �arf ekki a� kalla �a� tvisvar, og �� f� �g l�ka a� sj� hvort �a� er true e�a false.
				booking.printStatus();

			else
				cout << failedString; //Prentar �t fail string �egar �a� virkar ekki.
		}

		else if (procedure == "cancel") // Fyrir a� taka fr�.
		{
			if (booking.cancelReservations(id, cap) == true)
				booking.printStatus();

			else
				cout << failedString;
		}

		else if (procedure == "quit") // Fer �r loop, og h�ttir a� keyra forrit.
		{
			cout << "Logging out of service.";
			loop = false;

		}
		else
			cout << failedString;
	}

	return 0;
}



// NEW CODE HERE
// NEW
// NEW
// NEW 
// NEW
// NEW
// NEW 
// NEW


#include <iostream>
#include <sstream>
#include <iomanip> //Nota iomanip til �ess a� f� setprecision.
#include <math.h> //Nota math.h fyrir ceil.
using namespace std;

class FlightBooking {
public:
	FlightBooking(int id = 0, int capacity = 0, int reserved = 0);
	FlightBooking();
	void createFlight();
	void printStatus();
	bool reserveSeats(int flightID, int number_of_seats);
	bool cancelReservations(int flightID, int number_of_seats);
	int getID(int flightID);

private:
	int id;
	int capacity;
	int reserved;
};


FlightBooking::FlightBooking(int id, int capacity, int reserved)
{
	FlightBooking::id = id;
	FlightBooking::capacity = capacity;
	FlightBooking::reserved = reserved;
}

void FlightBooking::printStatus()
{

	float procentage = (float(reserved) / float(capacity)) * 100; //Breyti b��i breytunum � float svo a� �g get reikna� pr�sentuna.
	cout << "\n" << "Flight " << id << " : " << reserved << "/" << capacity << " (" << fixed << setprecision(0) << procentage << "%)  seats reserved" << "\n\n";
	//Kalla �essa runu til �ess a� prenta �t allt sem �g �arf + l�ka pr�sentut�luna me� �v� a� nota "setprecision(0)" til a� round-a t�luna
	//svo a� pr�sentan ver�ur ekki me� neina aukastafi, og "fixed" til �ess a� f� 'fixed floating-point notation'.
}

bool FlightBooking::reserveSeats(int flightID, int number_of_seats)
{
	float newReserved = float(reserved) + float(number_of_seats); //Geri n�ja breytu me� newReserved til �ess a� sleppa �v� a� sko�a tvisvar hvort �a� s� pl�ss fyrir fleiri reservations.
	float procentage = ceil((float(newReserved) / float(capacity)) * 100);
	//�essi breyta er notu� fyrir ne�an til a� sko�a hvort �a� s� h�gt a� b�ta vi� auka reservations.
	//�g nota l�ka "ceil" til a� round-a ni�ur svo a� �a� ver�ur ekki 15.x pr�sent. (�g m�tti r��a a� nota floor e�a ceiling.)
	if (procentage <= 105)
	{
		FlightBooking::reserved += number_of_seats; //B�ti vi� reservations.
		return true;
	}
	else
		return false;
}

bool FlightBooking::cancelReservations(int flightID, int number_of_seats)
{
	int checkReserved = (reserved - number_of_seats); //Nota �essa breytu fyrir ne�an til �ess a� sko�a hvort �g er me� n�g af resrvations til �ess a� fjarl�ga � burtu.
	if (checkReserved >= 0)
	{
		FlightBooking::reserved -= number_of_seats; //Fjarl�gi reservations ef �a� eru ekki undir 0.
		return true;
	}
	else if (checkReserved < 0) //Ef s�tin eru negat�f eftir �a� er b�i� a� fjarl�ga fr�, vistast s�tin sem 0.
	{
		FlightBooking::reserved = 0;
		return true;
	}
	else //Ef eitthva� fer �rskei�is.
		return false;
}

int FlightBooking::getID(int flightID)
{
	return this->id;
}


int main() {
	int arrsize = 1; // Heldur � array-size.
	int counter = 0; // Heldur � value � array.
	string failedString = "\n Cannot perform this operation \n\n";
	string fEdit; // Strengur sem heldur � user-input. fEdit stendur fyrir "Flight Edit"
	bool loop = true;
	int reserved = 0,
		capacity = 0;
	cout << "Provide flight capacity: ";
	cin >> capacity;
	cout << "Provide number of reserved seats: ";
	cin >> reserved;

	FlightBooking id1(1, capacity, reserved);
	FlightBooking *flightIDs[1]; // B� til n�tt array.
	flightIDs[0] = new FlightBooking(1, capacity, reserved);
	counter += 1;
	id1.printStatus();
	flightIDs[0]->printStatus();

	while (loop == true)
	{
		cout << "----------------------------------- \n";
		cout << "Welcome User. \n";
		cout << "You have 3 procedures available: \n";
		cout << "add [ID] [integer] \n";
		cout << "cancel [ID] [integer] \n";
		cout << "quit" << "\n \n";
		cout << "An example procedure would be: \n";
		cout << "add 1 4 \n";
		cout << "or \n";
		cout << "cancel 3 20 \n";
		cout << "----------------------------------- \n";

		cout << "Choose Procedure: ";
		getline(cin, fEdit);

		int id; // Velja flight number ID
		int cap; // Hversu marga � a� taka e�a setja inn.
		string procedure; // Taka fram hva� procedure �g nota.
		stringstream procedureString; // Setja svo � string stream.
		procedureString << fEdit;
		procedureString >> procedure >> id >> cap;

		if (procedure == "create")
		{
			bool idExist = false; // Boolean sem segir hvort id er til.
			for (unsigned int i = 0; i < sizeof(flightIDs) / sizeof(flightIDs[0]); i++)
			{
				if ((flightIDs[i]->getID(id)) == id)
				{
					idExist = true;
				}
			}

		}

		else if (procedure == "add") // Fyrir a� b�ta vi�
		{
			if (id1.reserveSeats(id, cap) == true) // �essi if-setning keyrir falli� � rauninni, �annig a� �g �arf ekki a� kalla �a� tvisvar, og �� f� �g l�ka a� sj� hvort �a� er true e�a false.
				id1.printStatus();

			else
				cout << failedString; //Prentar �t fail string �egar �a� virkar ekki.
		}

		else if (procedure == "cancel") // Fyrir a� taka fr�.
		{
			if (id1.cancelReservations(id, cap) == true)
				id1.printStatus();

			else
				cout << failedString;
		}

		else if (procedure == "quit") // Fer �r loop, og h�ttir a� keyra forrit.
		{
			cout << "Logging out of service.";
			loop = false;

		}
		else
			cout << failedString;
	}

	return 0;
}