# Automated Dollar General Survey Bot

I'm one of those people that enjoys the idea of filling out receipt surveys, but only for the sweepstakes at the end of it. But actually sitting down and 
doing the surveys has always been so boring. But I guess that's the point, so you have to really want to enter the sweepstakes...

Anyways, I finally got tired of filling out the surveys, and with Selenium's WebDriver, wrote a python program to do it for me. In my project, I'm using 
the Chrome WebDriver, but with some simple modification, you could use any other WebDriver you want, just please not IE, it really sucks. Believe me, I know.

## Future Improvements
This program is one of several automated survey bots I'm working on, and eventually I plan on combining all of them into a single program where I 
can select which company's survey I'm taking. Here are my other additions I plan on adding, so stay tuned:
* Single program for all companies I frequent
* GUI using PySimpleGUI (which is an amazing library btw)
* I'm sure there are other things I'm not thinking of

## Setting Up For Your Own Use
If you want to use this for your own purposes, you will need to make some modifications depending on how you want it set up.

**First**, decide which WebDriver you want to use. You will find a list of the ones available on Selenium's download page (https://www.selenium.dev/downloads/). 
Scroll down until you get to the *Browsers* dropdown and download the one for your preferred browser.

**Second**, there is this line in the code:
``` python
driver = webdriver.Chrome("../chromedriver")
```
If you are using chromedriver, then don't worry about changing it. But for my personal use, I have the chromedriver in the parent directory because I'm using the 
same one for several survey takers, and when Chrome updates, all I have to do is get the latest driver and replace it only once. I ***HIGHLY*** recommend this, 
but you do you.

**Thirdly**, this is not required, but if you are the only person using this program, you can go ahead and change these two lines from
``` python
name = input('First and Last Name (Joe Mama): ').split()
phone = input('Phone Number (555-555-5555): ')
email = input('Email: ')
```
to your own name and number. Just make sure they are both strings, and that the phone number **HAS** the dashes. Which brings up a good point, type the information in **EXACTLY AS SHOWN!** The program uses the split function to get the required information where it needs to go.

**Finally**, feel free to use this as a model for how to write your own survey bots. I found that there are a few surveys that use similar question ids, so you 
might get lucky and only have to change a few lines or variables.
