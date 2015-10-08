# I have two lists of names -- one list VPN usernames, 
# one list is all the email addresses of people who are no longer employed. 
# I want to write a script to tell me which VPN accounts to revoke 
# based on who is no longer employed.

# SAMPLE DATA
# LIST 1 -- Email Addresses of People Who are no longer employed
# bob@work.com
# suzie@work.com
# jen@work.com

# LIST 2 -- a complete list of VPN usernames
# vpn-tim
# vpn-jen
# vpn-clarence

# goal: return a list of vpn usernames for those no longer employed ex: [vpn-jen]

no_longer_employed = ['bob@work.com', 'suzie@work.com', 'jen@work.com']
all_vpn_accounts = ['vpn-tim', 'vpn-jen', 'vpn-clarence']

def sanitized_email(email_address) :
    """returns the username portion of the email address"""

def revoke_addresses(grads, vpn):
    revoke = []
    for email_address in grads:
        username = sanitized_email(email_address)
        vpn_username = "vpn-" + username
        if vpn_username in vpn:
            revoke.append(vpn_username)
    return revoke