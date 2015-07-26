__module_name__ = "Channel User Match Plugin"
__module_version__ = "0.1"
__module_description__ = "Return a list of users who match a given pattern for the currently open channel."
__author__ = "Thomas Ward"
__license__ = "GNU General Public License, v. 2.0"

import hexchat
import re

def _SplitPattern(pattern):
    # Effective pattern for current checking.  This gets modified as we go,
    # so we can't use the 'pattern' variable for this safely...
    ePattern = pattern
    
    # Build a list of [pNick, pIdent, pHost, pRealname] from
    # nick!ident@host#realname.
    
    # Nickname
    pNick = hexchat.strip(ePattern.split('!')[0], -1, 3)
    ePattern = ePattern.split('!')[1]
    
    # Ident
    pIdent = hexchat.strip(ePattern.split('@')[0], -1, 3)
    ePattern = ePattern.split('@')[1]
    
    # This is where it gets tricky...
    # Check if '#' (for realname) exists first
    if ('#' in pattern):
        # Host
        pHost = hexchat.strip(ePattern.split('#')[0], -1, 3)
        
        # Realname
        pRealname = hexchat.strip(ePattern.split('#')[1], -1, 3)

    else:
        # Host
        pHost = hexchat.strip(ePattern, -1, 3)
        
        # Realname not defined, assume "any"
        pRealname = '*'
        
    pattern_raw_segments = [pNick,pIdent,pHost,pRealname]
    return pattern_raw_segments
        
    
def _RegexPattern(pattern_raw_segments):
    rNick = re.escape(pattern_raw_segments[0]).replace('\*','.*')
    rIdent = re.escape(pattern_raw_segments[1]).replace('\*','.*')
    rHost = re.escape(pattern_raw_segments[2]).replace('\*','.*')
    rRealname = re.escape(pattern_raw_segments[3]).replace('\*','.*')
    
    pattern_regex_segments = [rNick,rIdent,rHost,rRealname]
    return pattern_regex_segments
    
    
def chanusermatch(word, word_eol, userdata):
    if (len(word) <= 1):
        print("You need to specify some pattern to match!")
    else:
        if (len(word) > 2):
            pattern = word_eol[1]
        else:
            pattern = word[1]
        
        if (('!' not in pattern) or ('@' not in pattern)):
            # This IRC Pattern is always enforced: nick!ident@host
            print("You need to specify a pattern in this form: nick!ident@host")
            print("You may specify a realname pattern if you wish by using the form: nick!ident@host#realname")
        else:
            rPattern = _RegexPattern(_SplitPattern(pattern))
            
            users = [user.nick for user in hexchat.get_list('users')
                     if re.match(r'%s' % rPattern[0], user.nick, flags=re.I) and 
                     re.match(r'%s@%s' % (rPattern[1],rPattern[2]),user.host,
                              flags=re.I) and
                     re.match(r'%s' % rPattern[3], user.realname, flags=re.I)]
            print('# of Matches: ' + str(len(users)))
            if (len(users) > 0):
                print(users)

    return hexchat.EAT_ALL
    
    
hexchat.hook_command("chanusermatch",chanusermatch)
hexchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
        
        


