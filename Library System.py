import webbrowser
import random
import time
class Library  :
    def __init__(self):
         pass 
    def get_info_employees() :
        name_of_employees = ["Maab" , "Malaz" ]
        ID_employees = [ "E20210001" , "E20210002" ] 
        database_of_employees = {}
        for i in range(len(name_of_employees)):
            database_of_employees[name_of_employees[i]] = ID_employees[i]
        for i in database_of_employees :
            print(f"Name: {i} , ID: {database_of_employees[i]}")
    def get_info_customrs():
        for i in range(len(name_of_customers)):
            database_of_customers[name_of_customers[i]] =ID_customers[i]
        for i in database_of_customers :
            print(f"Name: {i} , ID: {database_of_customers[i]}")
    def view_read_books():
           print("This is a list of read-only books :")
           num = 1
           for i in read_book :
            print(f" {num}.{i} : {read_book[i]}")
            num += 1
    def view_download_books():
        print("This is a list of books for download  :")
        num = 1
        for i in download_books :
                print(f" {num}.{i} : {download_books[i]}")
                num += 1
    def view_book_and_Author():
        print("These are all the books in the library :")
        num = 1
        for i in All_Books :
             print(f" {num}.{i} : {All_Books[i]}")
             num+=1
    def view_religious_lectures():
         print("These are all the religious lectures in the library :")
         num =1
         for i in Religious_lectures :
                        print(f"{num}. {i} ")
                        num+=1
    def view_podcast() :
         print("These are all the podcast in the library :")
         num = 1
         for i in view_list_of_podcast :
            print(f"{num}.{i}")
            num+=1
    def view_news_channels() :
        u = 1
        print("These are all  the channels in the library :")
        for i in view_list_of_News : 
                print(f"{u}.{i}")
                u+=1
    def Customer_reviews( ):
         ask = input("We are happy that you used our library. We'll take a few minutes of your time..... In order to improve our services, can you write your opinion about them or make suggestions\n")
         print("Thank you for your review\nGood bye")
         Customer_reviews.append(ask)
         
ID = 2021003
id = 2025006 
ID_and_Pass = {}
Customer_reviews = []
sign_time = time.ctime()
database_of_customers = {}
user_mail = ["malazeltag" ]
code= [2345,2576,6789,5676]
name_of_employees = ["Maab" , "malaz" ]
password_employees = [20210001,20210002]
ID_employees = [ "E20210001" , "E20210002" ] 
ID_customer =[2025001,2025002, 2025003 , 2025004,2025005 ]
password_Customer = [2025001,2025002,2025003,2025004,2025005 ]
name_of_customers = [ "sahar","walaa" ,"mona" , "fatima","mina"]
ID_customers = ["C2025001","C2025002" , "C2025003" , "C2025004","C2025005", ]
All_Books = {"Sarah Mohiuddin":"The Last Refuge Novel" , "Paulo Coelho" : "The Alchemist's Novel" , "Fyodor Dostoevsky": " White Nights Novel" , "Victor Hugo":  "Les Miserables Novel Part One" ," Mary Shelley": "Frankenstein's novel"
             ,"Dale Carnegie":" Book How to influence others and gain friends" , "Hull Alrod": " The Morning Miracle Book" ,"Brian Tracy ": " Goal Book"
             , "Ahmed Al Budeiri Al Hallaq " : "Damascus Daily Incidents Book" ,  "Arnold Toynbee" : "Human History Book" ,  "Yousef Al Esh " : " Book of the Umayyad dynasty" }

read_White_Nights = "https://www.kotobati.com/book/reading/7bba03c6-ff29-4278-8103-182f62976bd0" # قراءة كتاب  الليالي البيضاء 
read_Last_Refuge = "https://www.kotobati.com/book/reading/64ee24c0-cd4a-41cc-abdc-69ed7c4e92d9" #قراءة  كتاب الملجأ الاخير 
read_The_Alchemist = "https://www.kotobati.com/book/reading/768546b7-ac91-4df5-a60e-d4efb34af9d4" #قراءة كتاب الخيميائي 
read_Les_Miserables = "https://www.kotobati.com/book/reading/d11848ce-7f7f-411c-8201-eb44976aa377" #قراءة كتاب البؤساء 
read_Frankenstein = "https://www.kotobati.com/book/reading/5f3b0602-1706-4597-84fd-3e966096f5bd"  #قراءة رواية فرانكشتاين 
read_Book_How_to_influence_others_and_gain_friends = "https://www.kotobati.com/book/reading/f7c1f56d-c6d0-4026-ae1f-5c0dd9afee5a" #قراءة كتاب كتاب كيف تؤثر على الآخرين وتكتسب الأصدقاء      
read_The_Morning_Miracle_Book = "https://www.kotobati.com/book/reading/b13493a0-1c19-4c8e-b62f-4cf9abacc737"# قراءة كتاب معجزة الصباح
read_Goal_Book ="https://www.kotobati.com/book/reading/3d602ea2-990c-4dd1-b9ce-cc402fd0fe86" #قراءة كتاب الأهداف  
read_Damascus_Daily_Incidents_Book=  "https://www.kotobati.com/book/reading/0ae8c897-a2bb-4c56-b13a-fb6a00d18e26" #قراءة  كتاب حوادث دمشق اليومية
read_Human_History_Book =  "https://www.kotobati.com/book/reading/eee0014a-26cf-477d-9e96-b867beab007d"# قراءة كتاب تاريخ البشرية 
read_Book_of_the_Umayyad_dynasty = "https://www.kotobati.com/book/reading/c4490d14-b537-4140-9b1d-b093b900d032"# قراءة كتاب الدولة الاموية 

read_only = {"1": read_Last_Refuge ,"2" :read_The_Alchemist  , "3": read_White_Nights , "4":   read_Les_Miserables ,"5": read_Frankenstein
             ,"6":read_Book_How_to_influence_others_and_gain_friends , "7": read_The_Morning_Miracle_Book ,"8": read_Goal_Book
             , "9" : read_Damascus_Daily_Incidents_Book, "10" : read_Human_History_Book ,  "11" : read_Book_of_the_Umayyad_dynasty }
read_book = {"Sarah Mohiuddin":"The Last Refuge Novel" , "Paulo Coelho" : "The Alchemist's Novel" , "Fyodor Dostoevsky": " White Nights Novel" , "Victor Hugo":  "Les Miserables Novel Part One" ," Mary Shelley": "Frankenstein's novel"
             ,"Dale Carnegie":" Book How to influence others and gain friends" , "Hull Alrod": " The Morning Miracle Book" ,"Brian Tracy ": " Goal Book"
             , "Ahmed Al Budeiri Al Hallaq " : "Damascus Daily Incidents Book" ,  "Arnold Toynbee" : "Human History Book" ,  "Yousef Al Esh " : " Book of the Umayyad dynasty" }

download_White_Nights = "https://www.kotobati.com/book/download/7bba03c6-ff29-4278-8103-182f62976bd0" #تحميل كتاب الليالي البيضاء 
download_Last_Refuge= "https://www.kotobati.com/book/download/64ee24c0-cd4a-41cc-abdc-69ed7c4e92d9" #تحميل كتاب الملجأ الاخير 
download_The_Alchemist = "https://www.kotobati.com/book/download/768546b7-ac91-4df5-a60e-d4efb34af9d4 " #تحميل كتاب الخيميائي 
download_Les_Miserables = "https://www.kotobati.com/book/download/d11848ce-7f7f-411c-8201-eb44976aa377" #تحميل كتاب البؤساء 
download_Frankenstein ="https://www.kotobati.com/book/download/5f3b0602-1706-4597-84fd-3e966096f5bd" #تحميل  رواية فرانكشتاين 
# # التنمية البشرية 
download_Book_How_to_influence_others_and_gain_friends = "https://www.kotobati.com/book/download/f7c1f56d-c6d0-4026-ae1f-5c0dd9afee5a"# تحميل  كتاب كتاب كيف تؤثر على الآخرين وتكتسب الأصدقاء
download_The_Morning_Miracle_Book = "https://www.kotobati.com/book/download/b13493a0-1c19-4c8e-b62f-4cf9abacc737" #تحميل كتاب معجزة الصباح
download_Goal_Book = "https://www.kotobati.com/book/download/3d602ea2-990c-4dd1-b9ce-cc402fd0fe86" #تحميل كتاب كتاب الأهداف 
# # التاريخ 
download_Damascus_Daily_Incidents_Book = "https://www.kotobati.com/book/download/0ae8c897-a2bb-4c56-b13a-fb6a00d18e26" #تحميل كتاب حوادث دمشق اليومية
download_Human_History_Book  = "https://www.kotobati.com/book/download/eee0014a-26cf-477d-9e96-b867beab007d"  #تحميل  كتاب تاريخ البشرية 
download_Book_of_the_Umayyad_dynasty = "https://www.kotobati.com/book/download/c4490d14-b537-4140-9b1d-b093b900d032" #تحميل  كتاب الدولة الاموية 

download_Book = {"1": download_Last_Refuge ,"2" :download_The_Alchemist  , "3": download_White_Nights , "4":   download_Les_Miserables ,"5": download_Frankenstein
             ,"6":download_Book_How_to_influence_others_and_gain_friends , "7": download_The_Morning_Miracle_Book ,"8": download_Goal_Book
             , "9" : download_Damascus_Daily_Incidents_Book, "10" : download_Human_History_Book ,  "11" : download_Book_of_the_Umayyad_dynasty }
download_books = {"Sarah Mohiuddin":"The Last Refuge Novel" , "Paulo Coelho" : "The Alchemist's Novel" , "Fyodor Dostoevsky": " White Nights Novel" , "Victor Hugo":  "Les Miserables Novel Part One" ," Mary Shelley": "Frankenstein's novel"
             ,"Dale Carnegie":" Book How to influence others and gain friends" , "Hull Alrod": " The Morning Miracle Book" ,"Brian Tracy ": " Goal Book"
             , "Ahmed Al Budeiri Al Hallaq " : "Damascus Daily Incidents Book" ,  "Arnold Toynbee" : "Human History Book" ,  "Yousef Al Esh " : " Book of the Umayyad dynasty" }

Why_the_book_of_disease_and_cure  = "https://www.youtube.com/watch?v=4WknYA9zcNY&list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c&index=1&pp=iAQB"     #1
# " اخطر انواع المسكنات "
The_most_dangerous_types_of_painkillers  = "https://www.youtube.com/watch?v=TpgokChqa8Y&list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c&index=2&pp=iAQB" #2
# "تشخيص الداء اضرار الذنوب والمعاصي"
Diagnosis_of_disease_and_damage_to_sins   = "https://youtu.be/Tcm6r_RwdSE?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c" #3
# المرض الفتاك
deadly_disease = "https://youtu.be/Tf2Qkt8LxxY?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c" #4
#   المعاصي تدمرك  
Sins_destroy_you = "https://youtu.be/T6fq_FnfufA?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c" #5
# لماذا خلقنا؟ لماذا الابتلاءات ؟
Why_were_we_created_And_why_the_trials = "https://youtu.be/lUm87adLucI?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c" #6
# مداخل الشيطان 
devil_entrances = "https://www.youtube.com/watch?v=4oKWzrlP_lk&list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c&index=7&pp=iAQB " #7
# طبيعة الصراع بين الشيطان والانسان 
The_nature_of_the_conflict_between_devil_and_humans = "https://youtu.be/awLoljImWxM?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c"#8
# كيف تصل للقلب السليم 
How_to_reach_a_healthy_heart  = "https://www.youtube.com/watch?v=XtAQ91yq5cA&list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c&index=9&pp=iAQB"#9
# اعظم الذنوب 
The_greatest_sins = "https://www.youtube.com/watch?v=1QkDJjVz2Jw&list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c&index=10&pp=iAQB"#10
# الحصون الاربعة لحماية مداخل الشيطان 
The_Four_Forts = "https://youtu.be/G7tYFiN8mc4?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c"#11
# الشهوة الحرام 
Forbidden_lust = "https://youtu.be/sKADbvo7WuE?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c" #12
# الدواء الجامع لكل داء"
The_comprehensive_medicine_for_every_disease = "https://youtu.be/EK9_-0Cdfwk?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c"     #13
# صراع العقل والهوى 
The_struggle_of_mind_and_passion = "https://youtu.be/OEW400fgTac?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c" #14
#  العشق المحرم وعلاجه 
Forbidden_love = "https://youtu.be/ztt5JMzfDFA?list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c" #15
# الحب الحلال 
Halal_love =  "https://youtu.be/JDVGTFc2vPQ?si=UH4VIx1r6veMKKM9" #16
# لا تخبرها بانك تحبها  #
Don_not_tell_her_you_love_her  = "https://www.youtube.com/watch?v=EWSiNOfxlUE&list=PL1i_D1Vw3d5PBeIjJipobiLY1y4VKyg9c&index=17&pp=iAQB" #17
Religious_lectures =  [ "Why the book of disease and cure " , "The most dangerous types of painkillers", "Diagnosis of disease and damage to sins" ,"deadly disease ,", "Sins destroy you" , "Why were we created And why the trials","devil entrances ", "The nature of the conflict between devil and humans ","How to reach a healthy heart","The greatest sins","The Four Forts" ,"Forbidden lust","The comprehensive medicine for every disease" ,"The struggle of mind and passion","Forbidden love" ,"Halal love ","Don not tell her you love her "]
list_of_Lectures =  {"1":Why_the_book_of_disease_and_cure , "2": The_most_dangerous_types_of_painkillers, "3":Diagnosis_of_disease_and_damage_to_sins , 
                     "4": deadly_disease ,"5" :Sins_destroy_you , "6" : Why_were_we_created_And_why_the_trials, "7" : devil_entrances , 
                     "8" : The_nature_of_the_conflict_between_devil_and_humans ,"9": How_to_reach_a_healthy_heart,"10" :The_greatest_sins, 
                     "11" :The_Four_Forts ,"12" : Forbidden_lust ,"13" :The_comprehensive_medicine_for_every_disease , 
                     "14" : The_struggle_of_mind_and_passion, "15" : Forbidden_love, "16" : Halal_love ,"17" :Don_not_tell_her_you_love_her}
# بودكاست 
# "إيه المشكلة في ال حب و الارتباط ؟ 
What_is_the_problem_with_love_and_entering_into_relationships  = "https://youtu.be/AjUo-SJ5TSA?si=XHkKhteHHisQUx7R"
#   يه المشكلة في الأستعداد لرمضان ؟ 
What_is_the_problem_in_preparing_for_Ramadan = "https://youtu.be/COgiGghxxxI?si=VL72Xy8bQrfVu85e"
#  ايه المشكلة في الحجاب ولبس البنات ؟
What_is_the_problem_with_the_hijab_and_the_clothes_of_girls = "https://youtu.be/xBmwFnhx4I4?si=ucJted5X5oOq5HE8"
# إيه المشكلة في ذنوب الخلوات. ؟"
What_is_the_proble_with_the_sins_you_commit_when_you_are_alone   = "https://youtu.be/yqOJ8gDpgww?si=-yPaQ_ZmZFDZ92nZ"
# كيف تنجح العلاقات مع ياسر الحزيمي
How_relationships_succeed = "https://youtu.be/pJ0auP7dbcY?si=gubT9rMrvmstJHjQ"
# ماذا عبد العرب قبل الإسلام 
What_did_the_Arabs_worshipped_before_Islam = "https://youtu.be/hxut8_uuWho?si=ydH_cfNKuyqyoCcV"
# هل أنت مكتئب فعلًا"
Are_you_really_depressed  = "https://youtu.be/IDbMd2cVA8I?si=1WvZQPJTpl3nzRMy"

view_list_of_podcast = [ "How relationships succeed","Are you really depressed ?","What did the Arabs worshipped before Islam","What is the problem in preparing for Ramadan?", "What is the problem with the hijab and the clothes of girls?" ,"What is the problem with love and entering into relationships?" , "What is the problem with the sins you commit when you are alone?" ]
list_of_podcast =  {"1": How_relationships_succeed, "2": Are_you_really_depressed, "3":What_did_the_Arabs_worshipped_before_Islam , "4": What_is_the_problem_in_preparing_for_Ramadan ,
                    "5" :What_is_the_problem_with_the_hijab_and_the_clothes_of_girls , "6" :    What_is_the_problem_with_love_and_entering_into_relationships , "7" : What_is_the_proble_with_the_sins_you_commit_when_you_are_alone }
# الحدث 
AlHadath_Live_Stream = "https://www.youtube.com/live/w38Bna72qaw?si=b0HxY3hmdmAd8sBV"
# الجزيرة
Al_Jazeera_Arabic_Live = "https://www.youtube.com/live/bNyUyrR0PHo?si=a73bgYSVCJVsNFd_"
#  العربية 
AlArabiya_Livestream = "https://youtu.be/n7eQejkXbnM"
# LIVE_NEWS
LiveNOW_from_FOX = "https://youtu.be/YDfiTGGPYCk"
CNN_News18= "https://youtu.be/8EPO0voDduU"
# BBC_NEWS 
BBC_NEWS_Arabic = "https://youtu.be/dsivequqb-Q"
list_of_News =  {"1": AlHadath_Live_Stream , "2" : Al_Jazeera_Arabic_Live ,"3" :AlArabiya_Livestream ,
                  "4" : LiveNOW_from_FOX , "5" : CNN_News18, "6" :BBC_NEWS_Arabic }
view_list_of_News = ["Al Hadath Live Stream" , "Al Jazeera Arabic Live" , "Al Arabiya Livestream" , "LiveNOW from FOX English" , "CNN News 18 English" , "BBC NEWS Arabic" ]
while True :      
    try:
        print("Welcome to kotobati liberary , what do you want?\n1.creat account \n2.Login\n3.Exit")
        Register =int( input ("Enter Number  as 1 , 2\n"))
        if Register == 1:  
           name_ = input("Enter  your Name : 'Enter string just '\n")
           add = 1
           for o in  name_of_customers:
                if o == name_  :
                    print("The Name already exists in the list")
                    add = 0
                    break
                elif o != name_ :
                    add = 1
           if add == 1:        
                    name_of_customers.append(name_)
                    # print(name_of_customers)
           else:
                    ask_ =int(input("Do you want try again ?\n1.Yes\n2.No\n"))
                    if ask_ == 1:
                         continue
                    elif ask_ == 2 :
                         print("Good bye😊")
                         break
                    else:
                         print("Invalid input")
                         break
           year = int(input("your year's birth :"))
           number=(2025-year)  
           if  number <= 16  :
               print("you are under age 😕 You can\'t open separate account but... ")
               parents= input("Enter name of one of your parents :")
               email = input("Enter Your parents mail : ")
               add = 1
               for o in  user_mail:
                    if o == email  :
                        print("The Email already exists in the list")
                        add = 0
                        break
                    elif o != email :
                        add = 1
               if add == 1:        
                    user_mail.append(email)
                    # print(user_mail)
               else:
                    ask_ =int(input("Do you want try again ?\n1.Yes\n2.No\n"))
                    if ask_ == 1:
                         continue
                    elif ask_ == 2 :
                         print("Good bye😊")
                         break
                    else:
                         print("Invalid input")
                         break
               print(random.choice(code))
               confirmation_code=int(input("Enter confirmation code:"))
               if  confirmation_code in code :
                   print ("Been confirmed 🎉 ")
               else:
                   print("Verification Error")
                   ans=int(input("DO you want to try again?\n1.Yes\n2.No\n"))
                   if ans==1 :continue
                   print("")
                   if ans== 2 :    
                       print("Thank you") 
                       break
                   else :
                       break
               password = int(input("'Use numbers only'\npassword : "))  
               password_verification = int(input("Verify password: " ))
               if password == password_verification:
                   print ("You have been successfully signed up!" ) 
                   password_Customer.append(password)
                #    print(password_Customer)
                   new = 1
                   for p in ID_customer:
                       if p == id  :
                           id = ID_customer[-1]
                           id+=1 
                   print(f"your ID is : C{id}")    
                   ID_customer.append(id)
                   ID_customers.append(str(f"C{id}"))   
                   print(ID_and_Pass)
                   print(ID_customers)
                   print (f"you are creat your accont in {sign_time}")
                   ask = int(input("what do you want ?\n1.login now\n2.Exit the library "))
                   if ask == 1 :
                        continue
                   elif ask == 2 :
                        print("Thank you for choosing us ♥️ ")
                        break
               else:
                   print ("The password and the password verification don't match! Please try again")
                   ans=int(input("DO you want to try again? 'select 1 or 2'\n1.Yes\n2.No\n"))
                   if ans== 1 :continue
                   print("")
                   if ans==  2 :  
                        print("Good bye😊")
                        break
           else:
                    month=int(input("Month:"))
                    if month  < 13 :
                        print("",end="")
                    else:
                         print("please enter a number from 1 to 12")
                         break
                    birthday=int(input("day:" ) )
                    if month == 2 :
                         if birthday <= 29:
                              print("",end="")
                         else:
                            print("please enter a number from 1 to 28")
                            ans=int(input("DO you want to try again?\n1.Yes\n2.No\n"))
                            if ans==1 :continue
                            print("",end="")
                            if ans== 2 :    
                                print("Thank you") 
                            break
                         break  
                    if birthday <= 31 :
                         print("",end="")
                    else:
                         print("please enter a number from 1 to 31")
                         break
                    email_ = input("Enter your email :")
                    add = 1
                    for p in  user_mail:
                        if p == email_  :
                            print("The Email already exists in the list")
                            add = 0
                            break 
                        if p != email_ :
                            add = 1
                    if add == 1:        
                            user_mail.append(email_)
                    else:
                         ask_ =int(input("Do you want try again ?\n1.Yes\n2.No\n"))
                         if ask_ == 1:
                              continue
                         elif ask_ == 2 :
                              print("Good bye😊")
                              break
                         else:
                              print("Invalid input")
                              break
                    print(random.choice(code))
                    confirmation_code=int(input("Enter confirmation code:"))
                    if  confirmation_code in code :
                        print ("Been confirmed 🎉 ")
                    else:
                        print("Verification Error")
                        ans=int(input("DO you want to try again?\n1.Yes\n2.No\n"))
                        if ans==1 :continue
                        print("",end="")
                        if ans== 2 :    
                          print("Thank you") 
                          break
                    password_ =int( input("'Use numbers only'\npassword :"))  
                    password_verification = int(input("Verify password :" ))
                    if password_ == password_verification:
                        print ("You have been successfully signed up! 🎉🎊" )
                        password_Customer.append(password_)
                        print(password_Customer)
                        print (f"you are creat your accont in {sign_time}")    
                        new = 1
                        for p in ID_customer:
                           if p == id  :
                               id = ID_customer[-1]
                               id+=1 
                        print(f"your ID is : C{id}")    
                        ID_customer.append(id)
                        ID_customers.append(str(f"C{id}"))
                        for i in range(len(ID_customers)):
                            ID_and_Pass[ID_customers[i]] =password_Customer[i]
                        print(ID_and_Pass)
                        print(ID_customers)
                        ask = int(input("what do you want ?\n1.login now\n2.Exit the library\n"))
                        if ask == 1 :
                            continue
                        elif ask == 2 :
                            print("Thank you for choosing us ♥️ ")
                        break
                    else:
                        print ("The password and the password verification don't match! Please try again")
                        ans=int(input("DO you want to try again? 'select 1 or 2'\n1.Yes\n2.No\n"))
                        if ans== 1 :continue
                        print("")
                        if ans==  2 :  
                         print("Good bye😊")
                         break
        elif Register == 2 : 
            for i in range(len(ID_customers)):
                ID_and_Pass[ID_customers[i]] =password_Customer[i]
            for i in range(len(ID_employees)):
                ID_and_Pass[ID_employees[i]] =password_employees[i]
            # print(ID_and_Pass)
            login_ID = input("Enter your ID :")
            login_password = int(input("password :"))
            if login_ID  in ID_and_Pass and ID_and_Pass[login_ID] ==login_password :
                    print("You have been successfully logged in! ")
            else:
                  print("Incorrect password !")
                  ans=int(input("DO you want to try again?\n1.Yes\n2.No\n"))
                  if ans==1 :continue
                  print("",end="")
                  if ans== 2 :    
                      print("Thank you") 
                      break
                  break
            if login_ID in ID_employees :
                database_of_employees  ={ }
                for i in range(len(name_of_employees)):
                     database_of_employees[ID_employees[i]] = name_of_employees[i]
                if login_ID in  database_of_employees : 
                    print(f"\nHello {database_of_employees[login_ID]} ",end="") 
                print("Welcome to the library system\n")
                while True:
                    employees =int(input ( "To View List 'Enter 1 ' \nTo Add Item 'Enter 2 '\nTo Go To Last Page 'Enter 3'\n"))  
                    if employees == 1 :
                        View =int(input("\nwhat do you want to view? ' select number as  1 or 2 '\n1.View employees Data\n2.View customers Data\n3.view List of books\n4.view List of Podcast\n5.view List of News Channels\n6.view List of religious lectures\n7.view Customer reviews\n"))  
                        if View == 1 :
                            Library.get_info_employees()
                            ask = int(input("\nTo Go To Last Page ' Enter 1'\nTo Go Back Home 'Enter 2'\n"))
                            if ask == 1 :
                                 continue
                            elif ask  == 2:     
                               print("Have a Nice Day😊")
                               break
                        elif View == 2: 
                           Library.get_info_customrs()
                           ask = int(input("\nTo Go To Last Page ' Enter 1'\nTo Go Back Home  'Enter 2'\n"))
                    
                           if ask == 1 :
                                continue
                           elif ask  == 2:     
                              print("Have a Nice Day😊")
                              break
                        elif View == 3 :
                            Library.view_book_and_Author()
                            ask = int(input("\nTo Go To Last Page ' Enter 1'\nTo Go Back Home 'Enter 2'\n"))
                            if ask == 1 :
                                 continue
                            elif ask  == 2:     
                               print("Have a Nice Day😊")
                               break
                        elif View == 4 :
                            Library.view_podcast()
                            ask = int(input("\nTo Go To Last Page ' Enter 1'\nTo Go Back Home 'Enter 2'\n"))
                            if ask == 1 :
                                 continue
                            elif ask  == 2:     
                               print("Have a Nice Day😊")
                               break
                        elif View == 5:
                            Library.view_news_channels()
                            ask = int(input("\nTo Go To Last Page ' Enter 1'\nTo Go Back Home  'Enter 2'\n"))
                            if ask == 1 :
                                 continue
                            elif ask  == 2:     
                               print("Have a Nice Day😊")
                               break
                        elif View == 6:
                            Library.view_religious_lectures()
                            ask = int(input("\nTo Go To Last Page ' Enter 1'\nTo Go Back Home 'Enter 2'\n"))
                            if ask == 1 :
                                 continue
                            elif ask  == 2:     
                               print("Have a Nice Day😊")
                               break
                        elif View == 7:
                               print(Customer_reviews)
                               ask = int(input("\nTo Go To Last Page ' Enter 1'\nTo Go Back Home 'Enter 2'\n"))
                               if ask == 1 :
                                continue
                               elif ask  == 2:     
                                   print("Have a Nice Day😊")
                                   break
                    elif employees == 2 :
                        Add_ =int(input("\nwhat do you want to Add ? ' select number as  1 or 2 '\n1.Add books\n2.Add Podcast\n3.Add News Channels\n4.Add List of religious lectures\n ")) 
                        if Add_ == 1 :
                            print("\n         'To go to Back bage Enter '0'        \n")
                            while True:   
                                type_1 = int(input("1.read\n2.download\n3.Last Page\n"))
                                if type_1 == 3 :
                                    break
                                Author_add = input("Enter the name of the Author : ")
                                if Author_add == " 0" :
                                    break
                                book_add = input("Enter the name of the book : ")
                                URL_1 = input("Enter the book link : ")
                                add_1 = 1
                                for p in All_Books :
                                    if p == Author_add :
                                        print("The book already exists in the list")
                                        add_1 = 0
                                        break
                                    if p != book_add :
                                            add_1 = 1
                                if add_1 == 1:        
                                        All_Books[Author_add] = book_add
                                        print("The book has been added successfully")
                                if type_1 == 1 :
                                        num_1 = len(read_only) + 1 
                                        read_only[str(num_1)] = URL_1
                                        read_book[Author_add] = book_add
                                elif type_1 == 2 :
                                     num_2 = len(download_Book) + 1
                                     download_Book[str(num_2)] = URL_1
                                     download_books[Author_add] = book_add
                                else :
                                    print("Invalid Entery")
                                    break
                        elif Add_ == 2 :
                            print("\n         'To go to Back bage Enter '0'        \n")
                            while True:   
                                new_podcast = input("\nEnter the name of the new podcast: ")
                                if new_podcast == "0" :
                                    break
                                URL_2 = input("Enter the podcast link : ")
                                add_2 = 1
                                for i in view_list_of_podcast :
                                    if i == new_podcast :
                                        print("The podcast already exists in the list")
                                        add = 0
                                        break
                                    if i != new_podcast :
                                            add_2 = 1
                                if add_2 == 1:        
                                        print("The name has been added successfully\n")
                                        num_3 = len(view_list_of_podcast) + 1 
                                        list_of_podcast[str(num_3)] = URL_2
                                        view_list_of_podcast.append(new_podcast)
                                else :
                                    print("Invalid Entery")
                                    break
                        elif Add_ == 3 :
                            print("\n         'To go to Back bage Enter '0'        \n")
                            while True:   
                                new_channel = input("\nEnter the name of the new channel: ")
                                if new_channel == "0" :
                                    break
                                URL_3 = input("Enter the channel link : ")
                                add_3 = 1
                                for o in view_list_of_News :
                                    if o == new_channel :
                                        print("The channel already exists in the list")
                                        add_3 = 0
                                        break
                                    if o != new_channel :
                                            add_3 = 1
                                if add_3 == 1:        
                                        print("The channel has been added successfully\n")
                                        num_4 = len(view_list_of_News) + 1 
                                        list_of_News[str(num_4)] = URL_3
                                        view_list_of_News.append(new_channel)
                                else :
                                    print("Invalid Entery")
                                    break                
                        elif Add_ == 4 :
                            print("\n         'To go to Back bage Enter '0'        \n")
                            while True:   
                                new_lucture = input("\nEnter the name of the new lucture: ")
                                if new_lucture == "0" :
                                    break
                                URL_4 = input("Enter the lucture link : ")
                                add_4 = 1
                                for w in Religious_lectures  :
                                    if w == new_lucture :
                                        print("The lucture already exists in the list")
                                        add_4 = 0
                                        break
                                    if w != new_lucture :
                                            add_3 = 1
                                if add_4 == 1:        
                                        print("The lucture has been added successfully\n")
                                        num_5 = len(Religious_lectures) + 1 
                                        list_of_Lectures[str(num_5)] = URL_4
                                        Religious_lectures.append(new_lucture)
                                else :
                                    print("Invalid Entery")
                                    break                
                    elif employees == 3 :
                        break  
                    else :
                         print("Invalid choice! Please try again")
            elif login_ID in ID_customers :
                database_of_customer ={ }
                for i in range(len(name_of_customers)):
                     database_of_customer[ID_customers[i]] =   name_of_customers[i]
                if login_ID in  database_of_customer : 
                    print(f"\nHello {database_of_customer[login_ID]}, What do you want to show you?]\n ")    
                    while True :
                        choice = int(input("1.List of books \n2.List of religious lectures\n3.Podcast\n4.News Channels\n5.Exit\n"))
                        if choice == 1 :
                                More_Details = int(input("1.Read\n2.Download\n"))                         
                                if More_Details == 1 :
                                        Library.view_read_books()
                                        print("\n      Enter '0' To go to  Last list      \n") 
                                        while True :
                                            book_num = input("Enter the number of book :")
                                            if book_num == "0" :
                                                  break
                                            elif  book_num in read_only :
                                                    webbrowser.open(read_only [book_num])
                                            else:
                                                  print("\nChoose from the numbers in front of you only ")
                                                  ans = int(input("\nDo you want to search again ?\n1.Yes\n2.No\n"))
                                                  if ans == 1:
                                                    continue
                                                  elif ans == 2:
                                                       Library.Customer_reviews()
                                                       break
                                                  else :
                                                       print("Invalid Entery")
                                                       break
                                elif More_Details == 2 :
                                        # Library.view_book_and_Author()
                                        Library.view_download_books()
                                        print("\n         'To go to Back bage Enter '0'        \n")
                                        while True :
                                            book_num = input("Enter the number of book :")
                                            if book_num == "0":
                                                       break
                                            elif  book_num in download_Book :
                                                 webbrowser.open(download_Book [book_num])

                                            else:
                                               print("\nChoose from the numbers in front of you only\n")
                                               ans = int(input("\nDO you want to search again ?\n1.Yes\n2.No\n"))
                                               if ans == 1:
                                                  continue
                                               elif ans == 2:
                                                  Library.Customer_reviews()
                                                  break
                                               else :
                                                    print("Invalid Entery")
                                                    break
                                else : 
                                        print("\nInvalid choice! Please try again")
                        elif choice == 2 :
                            Library.view_religious_lectures()
                            print("\n         Enter '0' To go to Last page    \n")
                            while True :
                                lucture_num = input("Enter the number of lucture  :")
                                if lucture_num == "0":
                                          break
                                elif lucture_num  in list_of_Lectures :
                                   webbrowser.open(list_of_Lectures[lucture_num])
                                else :
                                   print("\nChoose from the numbers in front of you only")
                                   ans = int(input("\nDo you want to select again ?\n1.Yes\n2.No\n"))
                                   if ans == 1:
                                       continue
                                   elif ans == 2 :
                                        break
                                   else :
                                        print("\nInvalid Entery")
                                        break
                        elif choice == 3 :
                            Library.view_podcast()
                            print("\n         Enter '0' To go To Last page       \n")
                            while True :
                                podcast_num = input("Enter the number of podcast :  ")
                                if podcast_num == "0" :
                                          break
                                if podcast_num in list_of_podcast :
                                   webbrowser.open(list_of_podcast [podcast_num])
                                else:
                                    print("\nChoose from the numbers in front of you only")
                                    ans = int(input("do you want to select again ?\n1.Yes\n2.No\n"))
                                    if ans == 1:
                                     continue
                                    else:
                                     break
                        elif choice == 4 :
                            Library.view_news_channels()
                            print(" \n          Enter '0' To go To Last page         \n")
                            while True :
                                channel_num = input("Enter the number of channel :  ")
                                if channel_num == "0" :
                                          break
                                elif channel_num in list_of_News :
                                    webbrowser.open(list_of_News[channel_num])
                                else:
                                    print("\nChoose from the numbers in front of you only")
                                    ans = int(input("\ndo you want to select again ?\n1.Yes\n2.No\n"))
                                    if ans == 1:
                                     continue
                                    else:
                                     Library.Customer_reviews()
                                     break
                        elif choice == 5 :
                            Library.Customer_reviews()
                            break
                        else :
                            print("Invalid choice! Please try again")
            else :
                print("ID not found") 
                ans=input("Do you want to try again?'select 1 or 2'\n1.Yes\n2.No\n")
                if ans=="1" :continue
                print("")
                if ans== "2" :  
                    print("Good bye😊")
                    break
                else:
                    print("Invalid choice! Please try again")
        elif Register == 3:
            # Library.Customer_reviews()
            print("Good bye😊")
            break
        else:
            print("Invalid choice! Please try again")
    except:
        print("Invalid Entery")
        ans= input("DO you want to try again?'select 1 or 2'\n1.Yes\n2.No\n")
        if ans== "1" :
             continue 
        if ans == "2" :  
            print("Good bye😊")
            break
        else:
            print("Invalid Entery")
            break

#    https://www.kotobati.com/book/reading/3c748587-105c-435d-9890-8e0e4e8b5cfd
# Girl Wind اسم الرواية 
# Atheer Al , Abdullah
