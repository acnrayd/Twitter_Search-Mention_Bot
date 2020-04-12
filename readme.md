# Twitter Auto Search & Reply (without API) 

## What is it?

A script which tweets your website (link) to the Twitter users which have tweeted about your given keywords.

It is designed intentionally NOT TO USE official Twitter API - all actions are done by Selenium ChromeDriver.

## Why?

I was stuck in quarantine in an empty house, all alone, only with a bed, couch, computers and Internet connection. In weekdays I had a job to work, but weekends are totally free. Created a very simple website and disappointed with the visitor number. Decided to write a content marketing tool, started with Twitter auto reply bot.

Unfortunately it became one of my failed projects due to (very successful) Twitter algorithms for detecting spam bots. But anyway, fun to build, and I learned how to use Selenium. Cool!

## What it does?

0) Gets today's date.
1) Starts a Twitter search with the given keywords in the time period: Today.
2) Saves the usernames of the people tweeting about these keywords. (Default: 10 users for each keyword)
3) Logs in to your Twitter account. 
4) Waits for a random time. (between 5 and 30 secs)
5) Starts sending tweets to these targeted people and includes the link user has specified. It randomizes the content of the message so make sure that it will not include the same message in every Tweet.
6) Waits for a random time to continue with other people. (between 5 and 30 secs)
7) Continues with other keywords and links.
8) Quits the browser.

## How to use?

WARNING: What I have shared here might be against Twitter TOS. Using this script may get your Twitter account banned in less than half an hour!

NOTICE: Spamming & content-bombing might be illegal in your country. Use it at your own risk. 

1) Install Python 3.7.2
2) Install pip
3) Install Selenium and Twpy packages
4) Download Chromedriver for Selenium (choose the right version which works with your Chrome version: https://chromedriver.chromium.org/downloads)
5) Open the script main.py, read the first comment, add your own credentials, links and content.
6) Run main.py

# See in action!

Watch the video: https://streamable.com/luy82d

## DISCLAIMER

You have to be aware that you may violate Twitters Developer Agreement and Policy, Automation Rules and/or Twitter Rules - depending on how you configure it. If you don't configure it carefully your app will get suspended or even your account may get closed down by Twitter. Author of this script is not responsible for any action related to this.

The software is developed by a independent author without any professional expectations and released as open-source. Project will not be maintained for security vulnerabilities and feature enhancements. This product has no affiliations with the designated vendors. All product and company names are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them. THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


