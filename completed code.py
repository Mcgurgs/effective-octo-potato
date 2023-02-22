# A program to take user input and display information back based on input. Enjoy :) 

# Variables = user_name , user_password, user_color, user_pick, 
import time, sys
import colorama
from colorama import Fore, Back, Style 

colorama.init() 

# updates from previous code: 
# got rid of empyt print() 's
# added arg to type_text + got rid of type_text2 reddit reccomendation 
# added option to keep / stop colored text
# changed quit() -> sys.exit()



# typing effect 
def type_text(text, delay=0.02):            
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay) 


# Intro
def intro_func():
     type_text('Hello! Thanks for joining'.center(120))
     print('\n')
     type_text('Project #1'.center(120))
     print('\n\n')
     time.sleep(.03)
     type_text('              .-------.         \n')
     type_text( '.---------.   |  ===  |\n')
     type_text( '|.-"""""-.|   |  : :  |\n')
     type_text( '||   PC   |   |       |\n')
     type_text( '|-.....-. |   |:::::::|\n')
     type_text( '`\"\")---(")    |._____.|\n')
     type_text('/:::::::::::\" _"\n')
     type_text(':::=======:::/`/`/\n')
     type_text('`"""""""""""""`  -/\n')
     return ''
print(intro_func())

  
color_options = ['Blue','red','yellow','green','none']

# validating username
while True:
     type_text('What is your name? ')
     global user_name
     user_name = input().lower()
     if user_name.isalpha():
          break
     else:
          type_text('Please only enter letters in your name. ')

# validating user password
while True:
     type_text('Please create a password with letters and numbers')
     user_password = input()
     if user_password.isalnum():
          print('Account successfully created')
          break
     else: 
          type_text('Please use numbers and letters only. No special characters. ')

# add progress bar? 
time.sleep(.5)
print(f'\nNice to meet you, {user_name}.\n') 
type_text('What are your hobbies?')
print()
user_hobbies = input()
print()
type_text('Favorite color? Choose from the following options:  ')

# printing list 
for value in enumerate(color_options):
     print()
     print(value)

type_text('\nPlease input the index number of the color you would like. \'none\' will keep your text normal.\n')

# validate user input
while True: 
     try: 
          user_color = int(input())
          if user_color >= 0 and user_color <= 4:
               break 
          else:
               print('Invalid input. Please enter a number 0-4 ')
     except ValueError:
          print('Invalid input. Please input a valid number. ')

# outputting user_color 
if user_color == 0:
     type_text(Fore.BLUE + f'My personal favorite. Kudos {user_name} ')
     user_pick = (Fore.BLUE + 'Blue')
elif user_color == 1: 
     type_text(Fore.RED + 'Fun fact about red: It\'s the first color babies can see after black and white!.. I thought that was neat')
     user_pick = (Fore.RED + 'Red')
elif user_color == 2: 
     type_text(Fore.YELLOW + f'Yellow is a nice color. Good pick, {user_name} ')
     user_pick = (Fore.YELLOW + 'Yellow')
elif user_color == 3: 
     type_text(Fore.GREEN + f'Nice pick, {user_name} ')
     user_pick = (Fore.GREEN + 'Green')
else: 
     type_text('No changes have been applied ')
     user_pick = 'No favorite color '

# keep colors or stop 
while True:
     color_selection = input('\n\nWould you like to keep the colored text or stop the colored text? Options are : K (keep) | S (stop) ')
     if color_selection.upper() == 'K':
          type_text('Color has been kept!')
          break
     elif color_selection.upper() == 'S':
          type_text('Colored text has been turned off. ')
          print('\033[39m') #stops colored text
          break
     else: 
          print('That is not a valid option. Please enter: [K]|[S]')

print('\n\n') 
type_text(f'Current info:\n')

# display users info 
type_text(f'''             
            |                                                                
            |{user_name.center(60)}                                           
            |Password:{user_password[:2]}{"*" * (len(user_password) - 2)}
            |Hobbies: {user_hobbies}  
            |Color:   {user_pick}
             ''')

if color_selection == 'S':
     print('\033[39m')

# Dictionary of states 
states = {'Alabama':'Alabama is most known for it\'s Civil rights movement and history. Also Alabama is the hometown to several major NASA rocket engine testing facilities and astronaut training centers.',
          'Alaska':'Alaska has the largest coastline of any state in the US, stretching over 6,600 miles. It also has the highest mountain peak in North America, Mount Denali (formerly known as Mount McKinley), which is 20,310 feet tall.',
          'Arizona':'Arizona is home to the Grand Canyon, one of the Seven Natural Wonders of the World. The Grand Canyon is 277 miles long, up to 18 miles wide, and over a mile deep, making it one of the most spectacular geological formations in the world.',
          'Arkansas':'Arkansas is the only state in the US where diamonds are mined commercially. The first diamond was discovered in Arkansas in 1906, and the state has been a source of diamonds ever since.',
          'California':'California is known for its diverse geography, ranging from redwood forests and snowy mountains to sandy beaches and deserts. In fact, California has the largest economy of any state in the US, and is home to major industries such as technology, entertainment, and agriculture. Additionally, California produces more wine than any other state in the US and is home to over 1,200 wineries.',
          'Colorado':'Colorado is known for its beautiful mountain scenery and is a popular destination for outdoor activities such as skiing, hiking, and rafting. In fact, Colorado has the highest average elevation of any state in the US, with over 1,000 peaks that reach over 10,000 feet.',
          'Chicago':'Chicago is known for its architecture, including the Willis Tower (formerly known as the Sears Tower), which was the tallest building in the world when it was completed in 1973. The city is also known for its rich cultural history, including its blues and jazz music scenes. Additionally, Chicago is famous for its food, including deep-dish pizza, Italian beef sandwiches, and hot dogs with "dragged through the garden" toppings.',
          'Connecticut':'Connecticut is known for its beautiful countryside and small towns, as well as its rich maritime history and its role in the American Revolution.',
          'Delaware':'Delaware is known for being the first state to ratify the Constitution of the United States, making it the \"First State\".The state is also known for its rich history and colonial heritage, as well as its beautiful beaches and outdoor recreation areas.',
          'Florida':'Florida is known for its warm climate, beautiful beaches, and abundant wildlife. It is a popular tourist destination, attracting millions of visitors each year',
          'Georgia':'eorgia is known for its history and cultural heritage, including being the birthplace of Martin Luther King Jr. and being a key state in the American Civil Rights Movement.Additionally, Georgia is a major producer of peaches, pecans, and peanuts, and is sometimes referred to as the Peach State.',
          'Hawaii':'Hawaii is the only US state that is completely composed of islands and is located in the middle of the Pacific Ocean. The state is known for its beautiful natural scenery, including its volcanic landscapes, lush tropical forests, and stunning beaches.',
          'Idaho':'Idaho is known for its beautiful natural scenery, including its mountains, forests, and rivers. The state is a popular destination for outdoor activities such as hiking, skiing, and rafting, and is also known for its scenic hot springs and lakes. Additionally, Idaho is a major producer of potatoes and is sometimes referred to as the \"Potato State.\"',
          'Illinois':'Illinois is known for being a major transportation hub, with several major highways and waterways intersecting in the state, including the Mississippi River. Additionally, Illinois is a center of American history, with important events and figures such as Abraham Lincoln, the Underground Railroad, and the Chicago Fire all playing a role in shaping the state and the country.',
          'Indiana':'Indiana is known for its rich history and cultural heritage, including its role in the Underground Railroad. The state is also home to the Indianapolis 500, one of the most famous auto races in the world, and is sometimes referred to as the \"Racing Capital of the World\".',
          'Iowa':'Iowa is known for its fertile farmland and rich agricultural heritage, and is a leading producer of corn, soybeans, and other crops. Additionally, Iowa is a center of American history, with important events such as the Mormon Pioneer Trail and the Underground Railroad having taken place in the state',
          'Kansas':'Kansas is known for its beautiful prairies and rolling hills, as well as its rich agricultural heritage. The state is a leading producer of wheat, corn, and other crops, and is sometimes referred to as the \"Breadbasket of the World\".',
          'Kentucky':'Kentucky is known for its rich cultural heritage, including its bluegrass music, bourbon, and horse racing. The state is famous for being the birthplace of the Kentucky Derby, one of the oldest and most famous horse races in the world.',
          'Louisiana':'Louisiana is known for its rich cultural heritage, blending African, French, Spanish, and Native American influences to create a unique blend of customs and traditions. The state is famous for its Cajun and Creole cuisine, as well as its music, including jazz, blues, and zydeco. ',
          'Maine':'Maine is known for its beautiful natural scenery, including its rugged coastline, dense forests, and rolling hills. The state is a popular destination for outdoor activities such as hiking, fishing, and boating, and is also known for its scenic lighthouses and its lobsters, which are a major part of the state\'s economy and cuisine.',
          'Maryland':'Maryland is known for its rich history and cultural heritage, including its role in the American Revolution and its connections to important figures such as Francis Scott Key, who wrote the Star-Spangled Banner, and Harriet Tubman, who was born into slavery in the state and later escaped to become a leading abolitionist.',
          'Massachusetts':'Massachusetts is known for its rich history and cultural heritage, playing a key role in the American Revolution and being the birthplace of many important figures and events, including Paul Revere, the Boston Tea Party, and the first shots of the American Revolution at Lexington and Concord.',
          'Michigan':'Michigan is known for its beautiful natural scenery, including the Great Lakes, its dense forests, and rolling hills. Additionally, Michigan is an important center of industry, including the automobile industry, and is home to several major manufacturers, such as General Motors and Ford',
          'Minnesota':'Minnesota is known for its beautiful natural scenery, including its 10,000+ lakes, dense forests, and rolling hills. Additionally, Minnesota is a major center of industry and commerce, including manufacturing, finance, and healthcare.',
          'Mississippi':'Mississippi is known for its rich cultural heritage, blending African American, Native American, and European influences to create a unique blend of customs and traditions. The state is famous for its blues music, which originated in the Mississippi Delta region, and for its delicious cuisine, including southern favorites such as fried catfish, collard greens, and cornbread.',
          'Missouri':'Missouri is known for its rich history and cultural heritage, including its role in the American Civil War and its connections to important figures such as Mark Twain and Harry S. Truman. The state is also famous for its delicious cuisine, including barbecue and toasted ravioli, and for its beautiful natural scenery.',
          'Montana':'Montana is known for its beautiful natural scenery, including its rugged mountains, rolling prairies, and pristine lakes and rivers. Additionally, Montana is famous for its abundant wildlife, including grizzly bears, wolves, and herds of elk and bison.',
          'Nebraska':'Nebraska is known for its beautiful natural scenery, including its rolling prairies and expansive farmland. Additionally, Nebraska is an important center of agriculture, including farming and ranching, and is a major producer of crops such as corn, wheat, and soybeans.',
          'Nevada':'Nevada is known for its unique natural beauty, including its rugged deserts, mountain ranges, and hot springs. Additionally, Nevada is famous for its vibrant entertainment scene, including its world-renowned casinos and resorts, and its thriving arts and culture community.',
          'New Hampshire':'New Hampshire is known for its beautiful natural scenery, including the White Mountains, the Lakes Region, and the Seacoast. Additionally, New Hampshire is famous for its rich history and cultural heritage, including its role in the American Revolution and its connections to important figures such as Daniel Webster and Franklin Pierce.',
          'New Jersey':'New Jersey is known for its rich history and cultural heritage, including its role in the American Revolution and its connections to important figures such as Alexander Hamilton and Grover Cleveland. The state is also famous for its vibrant entertainment scene, including its world-renowned casinos and resorts, and its thriving arts and culture community.',
          'New Mexico':'New Mexico is known for its unique natural beauty, including its rugged deserts, mountain ranges, and hot springs. Additionally, New Mexico is famous for its rich cultural heritage, blending Native American, Spanish, and Mexican influences to create a unique blend of customs and traditions.',
          'New York':'New York is known for its rich history and cultural heritage, including its role in the American Revolution and its connections to important figures such as George Washington, Alexander Hamilton, and Abraham Lincoln. The state is also famous for its vibrant entertainment scene, including its world-renowned theaters, museums, and art galleries, and its thriving arts and culture community. Additionally, New York is a major center of commerce and industry, including finance, media, and technology, and is home to iconic landmarks such as the Statue of Liberty, Central Park, and the Empire State Building.',
          'North Carolina':'North Carolina is known for its rich history and cultural heritage, including its role in the American Revolution and its connections to important figures such as George Washington, Thomas Jefferson, and Andrew Jackson. The state is also famous for its beautiful natural scenery, including its rolling hills, pristine beaches, and lush forests.',
          'Ohio':'Ohio is known for its rich history and cultural heritage, including its role in the American Revolution and its connections to important figures such as William Henry Harrison and Ulysses S. Grant. The state is also famous for its beautiful natural scenery, including its rolling hills, pristine lakes, and lush forests. Additionally, Ohio is a major center of commerce and industry, including finance, healthcare, and education, and is home to several world-class universities and research institutions.',
          'Oklahoma':'Oklahoma is known for its cowboy colutre, Native American history, and beautiful scenery. Oklahoma is a huge contributor to the wind and energy sector. Would reccommend for a roadtrip!',
          'Oregon':'Oregon is famous for its amazing natural wonders like Crater Lake, Mount Hood, and Cannon Beach.',
          'Pennysylvania':'Pennysylvania is home to one the nation\'s most important industrial centers for railroads, coal, and steel since before WW2.',
          'Rhode Island':'Rhode Island is the smallest state in the U.S and is also one of the original U.S colonies!',
          'South Carolina':'South carolina is most known for its beaches, sunny weather, and is a very tourist busy area.',
          'South Dakota':'South Dakota is known for its state parks! There is Mount Rushmore, The Badlands, and Wind Cave. The state\'s nickname is \"The Mount Rushmore State\".',
          'Tennessee':'Tennessee is known for its whiskey, The Smokey Mountain National park in Gatlinburg, and its great music scene in Nashville!',
          'Texas':'Texas is known for hot weather, oil, and BBQ\'d food. Texas is also known for the JFK Assassination.',
          'Utah':'The state is known for it\'s national parks, skiing, and it\'s large mormon community.',
          'Vermont':'One interesting fact about Vermont is that it is the largest producer of maple syrup in the United States, and it actually produces more maple syrup than any other state in the country.',
          'Virginia':'Virginia is a state located in the southeastern part of the United States. It is known for its rich history and played a significant role in the founding of the United States.',
          'Washington':'Washington is known for its stunning natural beauty, including Mount Rainier, the Olympic Mountains, and the Puget Sound',
          'West Virginia':'West Virginia is a state located in the Appalachian region of the United States. It is known for its beautiful natural scenery, rich history, and distinctive culture. A small list: Mountains, outdoor rec, festivals, and its beauty.',
          'Wisconsin':'Wisconsin is a state located in the Midwest region of the United States. It is known for its natural beauty, distinctive culture, and diverse economy. It\'s known for several things, including cheese, beer, football, and its beautiful lakes and outdoor rec (my favorite hobby :D)',
          'Wyoming':'Wyoming is a state located in the western part of the United States, known for its stunning natural landscapes and rich history. It has lots of National parks and also know for its cowboy culture. There have also been many fossil finds, including several dinosaur species!'}
print('\n\n')

type_text('What State are you from? If outside of the U.S, enter which country!')
in_usa = input()
  
# searching for dictionary key
if in_usa in states:
          if in_usa in states:
            type_text('Checking database....\n')
            time.sleep(0.2)
            type_text(f'This is what we have for {in_usa}:  ')
            print('\n')
            type_text(states[in_usa]) # printing states info 

            # User input to add to state information 
            print('\n')
            time.sleep(1)
            type_text('Would you like to add to your state\'s info? If nothing, just slap enter.\n')
            state_update = input()
            if state_update:
                 states[in_usa] = states[in_usa] + ' ' + state_update  # doesnt update dict +
                 type_text('The states info has successfully been updated!\n')
                 print(states[in_usa])
            else: 
                 type_text('\nNo updates have been made')

 # progress bar much needed here           
else:
    type_text('I do not have info for that location\n')
    type_text(f'Please input something about {in_usa}\n')
    new_location = input()
    states[in_usa] = new_location
    type_text('Database updating:\n')
    type_text('10%..\n')
    time.sleep(.1)
    type_text('29%..\n') 
    time.sleep(.1)
    type_text('45%..\n')
    time.sleep(.2)
    type_text('70%..\n')
    time.sleep(.1)
    type_text('99%.....\n')
    time.sleep(.1)
    type_text('Database update complete!')
print('\n\n')

type_text('Would you like to see all of the states info?\n')

verify_input = input('Please select:|Y|-|N|\n').upper()

password_attempts = 3

# password check , 3 attempts or the game exits

while password_attempts > 0 and verify_input == 'Y':
    user_verification = input((f'Hello {user_name}, please enter the account password: '))
    
    if user_verification == user_password:
         type_text('Login Successful!\n ')
         time.sleep(0.2)
         break
    else: 
         password_attempts -= 1
         if password_attempts > 0: 
              type_text(f'Incorrect password. You have {password_attempts} attempts remaining. ')
         else:
              if password_attempts == 0: 
                type_text(' You have used all of your login attempts. Login failed. ')
                sys.exit()

print('\n\n\n')

for state, info in states.items():
    if verify_input == 'Y':
        print(f"{state}: {info}")
    else:
         type_text('Database will remain hidden')
         break 

print('\n\n\n')
    
type_text(f'\nI hope you enjoyed this small project. Thanks again for joining, {user_name}')
type_text('\nFind me on LinkedIn or Twitter')
type_text('\nLinkedIn: https://www.linkedin.com/in/kylermcguire/')
type_text('\nTwitter: https://twitter.com/heretolearnman')
print('\n\n')
time.sleep(10)
type_text('Cya!')
sys.exit()


