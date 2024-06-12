from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


name = ["Alan", "Murat", "Azad", "Necati", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan",
                 "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
                 "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed",
                 "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel",
                 "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam",
                 "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil",
                 "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed",
                 "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian",
                 "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay",
                 "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert",
                 "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs",
                 "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf",
                 "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider",
                 "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen",
                 "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan",
                 "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer",
                 "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs",
                 "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet",
                 "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio",
                 "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep",
                 "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez",
                 "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis",
                 "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran",
                 "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved",
                 "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley",
                 "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal",
                 "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun",
                 "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan",
                 "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub",
                 "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise",
                 "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley",
                 "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz",
                 "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz",
                 "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay",
                 "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod",
                 "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue",
                 "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony",
                 "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly",
                 "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee",
                 "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan",
                 "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody",
                 "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan",
                 "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak",
                 "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan",
                 "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Melim","Colman",
                 "Colver","Con","Conan","Conant","Conn","Conney","Connie","Connor","Conny","Conrad","Conrade","Conrado",
                 "Conroy","Consalve","Constantin","Constantine","Constantino","Conway","Coop","Cooper","Corbet","Corbett",
                 "Corbie","Corbin","Corby","Cord","Cordell","Cordie","Cordy","Corey","Cori","Cornall","Cornelius","Cornell",
                 "Corney","Cornie","Corny","Correy","Corrie","Cort","Cortie","Corty","Cory","Cos","Cosimo","Cosme","Cosmo",
                 "Costa","Court","Courtnay","Courtney","Cozmo","Craggie","Craggy","Craig","Crawford","Creigh","Creight",
                 "Creighton","Crichton","Cris","Cristian","Cristiano","Cristobal","Crosby","Cross","Cull","Cullan","Cullen"
                 ,"Culley","Cullie","Cullin","Cully","Culver","Curcio","Curr","Curran","Currey","Currie","Curry","Curt",
                 "Curtice","Curtis","Cy","Cyril","Cyrill","Cyrille","Cyrillus","Cyrus","Darcy","Dael","Dag","Dagny","Dal"
                 ,"Dale","Dalis","Dall","Dallas","Dalli","Dallis","Dallon","Dalston","Dalt","Dalton","Dame","Damian","Damiano"
                 ,"Damien","Damon","Dan","Dana","Dane","Dani","Danie","Daniel","Dannel","Dannie","Danny","Dante","Danya"
                 ,"Dar","Darb","Darbee","Darby","Darcy","Dare","Daren","Darill","Darin","Dario","Darius","Darn","Darnall"
                 ,"Darnell","Daron","Darrel","Darrell","Darren","Darrick","Darrin","Darryl","Darwin","Daryl","Daryle",
                 "Dav","Dave","Daven","Davey","David","Davidde","Davide","Davidson","Davie","Davin","Davis","Davon","Davy"
                 ,"De","Witt","Dean","Deane","Decca","Deck","Del","Delainey","Delaney","Delano","Delbert","Dell","Delmar"
                 ,"Delmer","Delmor","Delmore","Demetre","Demetri","Demetris","Demetrius","Demott","Den","Dene","Denis",
                 "Dennet","Denney","Dennie","Dennis","Dennison","Denny","Denver","Denys","Der","Derby","Derek","Derick"
                 ,"Derk","Dermot","Derrek","Derrick","Derrik","Derril","Derron","Derry","Derward","Derwin","Des","Desi"
                 ,"Desmond","Desmund","Dev","Devin","Devland","Devlen","Devlin","Devy","Dew","Dewain","Dewey","Dewie"
                 ,"Dewitt","Dex","Dexter","Diarmid","Dick","Dickie","Dicky","Diego","Dieter","Dietrich","Dilan","Dill"
                 ,"Dillie","Dillon","Dilly","Dimitri","Dimitry","Dino","Dion","Dionisio","Dionysus","Dirk","Dmitri",
                 "Dolf","Dolph","Dom","Domenic","D]","Elihu","Elijah","Eliot","Elisha","Ellary","Ellerey","Ellery",
                 "Elliot","Elliott","Ellis","Ellswerth","Ellsworth","Ellwood","Elmer","Elmo","Elmore","Elnar",
                 "Elroy","Elston","Elsworth","Elton","Elvin","Elvis","Elvyn","Elwin","Elwood","Elwyn","Ely","Em"
                 ,"Emanuel","Emanuele","Emelen","Emerson","Emery","Emile","Emilio","Emlen","Emlyn","Emmanuel",
                 "Emmerich","Emmery","Emmet","Emmett","Emmit","Emmott","Emmy","Emory","Engelbert","Englebert",
                 "Ennis","Enoch","Enos","Enrico","Enrique","Ephraim","Ephrayim","Ephrem","Erasmus","Erastus",
                 "Erek","Erhard","Erhart","Eric","Erich","Erick","Erie","Erik","Erin","Erl","Ermanno","Ermin",
                 "Ernest","Ernesto","Ernestus","Ernie","Ernst","Erny","Errick","Errol","Erroll","Erskine","Erv"
                 ,"ErvIn","Erwin","Esdras","Esme","Esra","Esteban","Estevan","Etan","Ethan","Ethe","Ethelbert",
                 "Ethelred","Etienne","Ettore","Euell","Eugen","Eugene","Eugenio","Eugenius","Eustace","Ev",
                 "Evan","Evelin","Evelyn","Even","Everard","Evered","Everett","Evin","Evyn","Ewan","Eward",
                 "Ewart","Ewell","Ewen","Ezechiel","Ezekiel","Ezequiel","Eziechiele","Ezra","Ezri","Fabe",
                 "Faber","Fabian","Fabiano","Fabien","Fabio","Fair","Fairfax","Fairleigh","Fairlie"]

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver= webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://www.youtube.com/")
time.sleep(5)
driver.find_element_by_id("avatar-btn").click()#icon click
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[4]/div[2]/ytd-compact-link-renderer/a/tp-yt-paper-item').click()#setting
time.sleep(6)
driver.find_element_by_css_selector('#options > ytd-channel-options-renderer > yt-formatted-string:nth-child(3) > a').click()
#driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-settings-options-renderer/div/div[2]/div/ytd-channel-options-renderer/yt-formatted-string[2]/a').click()#create a new channel
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(random.choice(name))#choose random name to create brand acc
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/label/span').click()#tick box
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[3]/input[2]').click()#create button
time.sleep(25)
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[4]/div[2]/ytd-compact-link-renderer/a/tp-yt-paper-item').click()
time.sleep(6)
driver.find_element_by_css_selector('#options > ytd-channel-options-renderer > yt-formatted-string:nth-child(3) > a').click()
#driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-settings-options-renderer/div/div[2]/div/ytd-channel-options-renderer/yt-formatted-string[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-switcher-page-renderer/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(random.choice(name))
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/label/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[3]/input[2]').click()
time.sleep(25)
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[4]/div[2]/ytd-compact-link-renderer/a/tp-yt-paper-item').click()
time.sleep(6)
driver.find_element_by_css_selector('#options > ytd-channel-options-renderer > yt-formatted-string:nth-child(3) > a').click()
#driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-settings-options-renderer/div/div[2]/div/ytd-channel-options-renderer/yt-formatted-string[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-switcher-page-renderer/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(random.choice(name))
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/label/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[3]/input[2]').click()
time.sleep(25)
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[4]/div[2]/ytd-compact-link-renderer/a/tp-yt-paper-item').click()
time.sleep(6)
driver.find_element_by_css_selector('#options > ytd-channel-options-renderer > yt-formatted-string:nth-child(3) > a').click()
#driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-settings-options-renderer/div/div[2]/div/ytd-channel-options-renderer/yt-formatted-string[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-switcher-page-renderer/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(random.choice(name))
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/label/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[3]/input[2]').click()
time.sleep(25)
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[4]/div[2]/ytd-compact-link-renderer/a/tp-yt-paper-item').click()
time.sleep(6)
driver.find_element_by_css_selector('#options > ytd-channel-options-renderer > yt-formatted-string:nth-child(3) > a').click()
#driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-settings-options-renderer/div/div[2]/div/ytd-channel-options-renderer/yt-formatted-string[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-switcher-page-renderer/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(random.choice(name))
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/label/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[3]/input[2]').click()
time.sleep(30)
#here i added upto creating 5 auto brand accounts create....