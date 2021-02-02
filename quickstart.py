# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'myrentshop'
insta_password = '0980500873ss'


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity		
  session.like_by_tags(["natgeo"], amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
