




def display_menu(): #this funtion is used to display the menu
    print("Iris Data Set")
    print("--------")
    print("MENU")
    print("====")
    print("1 – Introduction To Iris Data Set")
    print("2 - View Image Of Iris Varieties")
    print("-----------------------------------")
    print("3 – View Average Sizes Iris")
    print("4 – View Minimum Sizes Iris")
    print("5 – View Maximum Sizes Iris")
    print("-----------------------------------")
    print("6 – Save Summary Data To Text File")
    print("-----------------------------------")
    print("7 – View Paired Graph Plots")
    print("8 – View Scatter Plots")
    print("9 – View Histograms")
    print("-----------------------------------")
    print("10 – Save Paired Graph Plots")   
    print("11 – Save Scatter Plots")   
    print("12 – Save Histograms")
    print("-----------------------------------")
    print("x – Exit application")








# Main function , code was repurposed from lecture menu
def main():
    # Initialise array
    array = []
    display_menu() #This function calls the user menu



    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            clear_screen()
            Introduction_To_Iris_Data_Set()
            display_menu()
        elif (choice == "2"):
            clear_screen()
            View_Image_Of_Iris_Varieties()
            display_menu()
        elif (choice == "3"):
            clear_screen()
            View_Average_Sizes_Iris()
            View_Average_of_Setosa()
            View_Average_of_Versicolor()
            View_Average_of_Virginica()
            display_menu()
        elif (choice == "4"):
            clear_screen()
            View_Minimum_Sizes_Iris()
            View_Minimum_Sizes_Setosa()
            View_Minimum_Sizes_Versicolor()
            View_Minimum_Sizes_Virginica()
            display_menu()
        elif (choice == "5"):
            clear_screen()
            View_Maximum_Sizes_Iris()
            View_Maximum_Sizes_Setosa()
            View_Maximum_Sizes_Versicolor()
            View_Maximum_Sizes_Virginica()
            display_menu()
        elif (choice == "6"):
            clear_screen()
            Save_Summary_Of_Average_Iris_Sizes_To_Text_File()
            display_menu()
        elif (choice == "7"):
            clear_screen()
            View_Paired_Graph_Plots()
            display_menu()
        elif (choice == "8"):
            clear_screen()
            View_Data_As_Scatter_Plot()
            display_menu()
        elif (choice == "9"):
            clear_screen()
            View_Data_As_Histogram()
            display_menu()

        elif (choice == "10"):
            clear_screen()
            Save_Paired_Graph_Plots()
            display_menu()
            
        elif (choice == "11"):
            clear_screen()
            Save_Data_As_Scatter_Plot()
            display_menu()            

        elif (choice == "12"):
            clear_screen()
            Save_Data_As_Histogram()
            display_menu()
        elif (choice == "x"):
            break;
        else:
            display_menu()


if __name__ == "__main__":
    # execute only if run as a script
    main()
