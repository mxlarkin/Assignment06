#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
dicTbl = []  # list of dicationaries to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    '''Adding and deleting items from the CD inventory table stored during run time'''
    # TODone add functions for processing here

    @staticmethod
    def add_CD(title, artist, table):
        '''Function to add CD to 2D table, list of dics
        Args:
            cdID (string): string to add to dictionary
            title (string): string to add to dictionary
            artist (string): string to add to dictionary
            table (list of Dics): Table of dics to add new dictionary to
        Returns:
            None.
        '''
        cdID = len(dicTbl) + 1
        # intID = int(cdID)
        dicRow = {'ID': cdID, 'Title': title, 'Artist': artist}
        table.append(dicRow)
        
    @staticmethod
    def delete_CD(cdID, table):
        '''Function to delete CD in ED table, list of dics
        Args:
            cdID (Integer): ID number for CD in dictionary to delete from table
            table (list of dics): Table of dictionaries to delete dic from
        Returns:
            None.
        '''
        intRowNr = -1
        blnCDRemoved = False
        for row in dicTbl:
            intRowNr += 1
            if int(row['ID']) == intIDDel:
                del dicTbl[intRowNr]
                blnCDRemoved = True
                break
        for i in range(len(dicTbl)): # renumbers IDs to prevent duplicates after del row
           j = i + 1
           dicTbl[i]['ID'] = j
           
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')


class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        '''Function to write user data from a list of dictionaries to a file
        
        Processes data line by line from a dictionary into string form to then write to a 
        text file. 
        
        Args: 
            file_name: Name of file to save data from the 2D table used in run time to
            table: 2D data structure (list of dictionaries) that holds data during run time
        Returns:
            None.
        '''
        # TODone Add code here
        objFile = open(strFileName, 'w')
        for row in dicTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ''
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        #print('\n')  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # TODone add I/O functions as needed
    @staticmethod
    def input_CD():
        '''Get user input for CD to add
        Args:
            None
        Returns:
            strID (string): string of user input for new CD ID
            strTitle (string): string with user input for new CD title
            strArtist (string): string with user input for new CD artist
            '''
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return title, artist

# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, dicTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'y\' to continue and reload from file; otherwise reload will be cancelled:\n')
        if strYesNo.lower() == 'y':
            print('reloading...')
            FileProcessor.read_file(strFileName, dicTbl)
            IO.show_inventory(dicTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(dicTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # TODone move IO code into function
        strTitle, strArtist = IO.input_CD()
        # 3.3.2 Add item to the table
        # TODone move processing code into function
        DataProcessor.add_CD(strTitle, strArtist, dicTbl)
        IO.show_inventory(dicTbl)
        print('You must save the file to keep this change.')
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(dicTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(dicTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        # TODone move processing code into function
        DataProcessor.delete_CD(intIDDel, dicTbl)
        IO.show_inventory(dicTbl)
        print('You must save the file to keep this change.')
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(dicTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODone move processing code into function
            FileProcessor.write_file(strFileName, dicTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




