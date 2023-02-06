import time
import colorama 
from colorama import Fore, Back, Style 
colorama.init() 



# Game is based on user input - showing off my new founded skills - Validation , dictionaries, basic functions , the more I code , the more ideas that come to mind. Enjoy ->>
# typing effect function ->

def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05) # adjust the time delay here as needed

        # Intro
type_text('Hello, thanks for joining ..')
print()
time.sleep(.04)
type_text('My name is Kyler, I like nature, traveling, and computer science.')
print()
type_text('              .-------.         ')
print()
type_text( '.---------.   |  ===  |')
print()
type_text( '|.-"""""-.|   |  : :  |')
print()
type_text( '||   PC   |   | Gurgs |')
print()
type_text( '|-.....-. |   |:::::::|')
print()
type_text( '`\"\")---(")    |._____.|')
print()
type_text('/:::::::::::\" _"')
print()
type_text(':::=======:::/`/`/')
print()
type_text('`"""""""""""""`  -/')
print()
print()
print()
type_text('What is your name?')
print()
name = str(input())
time.sleep(1)
print()
print(f'Hi {name} :D')
type_text('Tell me something you like doing ')
user_hobby = input()
print()
type_text('Thanks for sharing')
time.sleep(1)
print()
print()
type_text('Please choose a color from the following options: ')

color_options = ['Blue','red','purple','green','none']           # List of colors 

type_text('Please input the index number of the color you would like. \'none\' will keep your text normal.')

for index, value in enumerate(color_options):
     print()
     print(f'{index} - {value}')

# validate user input
while True: 
        try: 
            user_color = int(input())
            if user_color >= 0 and user_color <= 4:
                break 
            else:
                print('Invalid input. Please enter a number 0-4')
        except ValueError:
            print('Invalid input. Please input a valid number.')

type_text(f'Thanks {name}, \n Your pick: {user_color}! \n Color changing functionality will be available later on :) ')


print()
print()
print()

# print(Fore.RED + 'some red text') -  I want to ask for favorite color, change text to that color 



# *add states - 2/6/ GET DONE  
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
          'Vermont':'',
          'Virginia':'',
          'Washington':'',
          'West Virginia':'',
          'Wisconsin':'',
          'Wyoming':''}

print('What state are you from?')
print()
in_usa = input()
  

if in_usa in states:
          if in_usa in states:
            print('Checking database....')
            time.sleep(5)
            print(f'This is what we have for {in_usa}: ')
            print()
            type_text(states[in_usa]) # prints states info 

            # adding user input , lets them add something about state if they want , also option to add none
            time.sleep(1)
            print()
            print()
            print('Would you like to add to your state\'s info? Enter nothing if no.')
            print()
            state_update = input()
            if state_update:
                 states[in_usa] = states[in_usa] + '  updated info :' + state_update  # doesnt update dict +
                 print('The states info has successfully been updated!')
                 print()
                 print(states[in_usa])
            else: 
                 print('No updates have been made')
           
else: # will add state
    type_text('I do not have info for that location')
    print()
    type_text(f'Can you tell me something about {in_usa}?')
    print()
    new_location = input()
    print()
    states[in_usa] = new_location
    type_text(' Database updating..')
    print()
    type_text('10%..')
    print()
    time.sleep(1)
    type_text('29%') 
    print()
    time.sleep(1.5)
    type_text('45%..')
    print()
    time.sleep(1.5)
    type_text('70%..')
    print()
    time.sleep(1.5)
    type_text('99%.....')
    print()
    time.sleep(2)
    type_text('Database update complete!')
print()
type_text('Would you like to see the database contents?')
print()
print('Please select:|Y|-|N|')
verify_input = input().upper()

if verify_input == 'Y':
    type_text(f'Welcome to the database {name} ')
    type_text('__________________________________')
    print()
    print()
    print(states.keys())
    print()
    print()
    type_text('__________________________________')
if verify_input == 'N':
     print('Database contents will remain hidden.')

type_text('Here is your info, {name} :  ')

# 'No' options work 

# box with users info , 
