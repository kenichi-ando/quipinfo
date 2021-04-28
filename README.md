# quipinfo

This script shows Quip document's attributes.

## How to use
1. Get an access token from https://quip.com/dev/token.
2. Set the token to QUIP_ACCESS_TOKEN environment variable. (EXPORT QUIP_ACCESS_TOKEN="_YOUR-ACCESS-TOKEN_")
3. Copy a 12-character URL suffix from a Quip's document URL. (e.g. X1fcAZdhTyNp)
4. Run the script by python3 with the suffix value.

```
% ./quipinfo.py X1fcAZdhTyNp
   Thread ID: KKVAAAiB2Js
         URL: https://your-domain.quip.com/X1fcAZdhTyNp
       Title: Document Title
        Type: document
      Author: Quip Admin
Created Date: 2021-03-19 10:08:30
Updated Date: 2021-04-19 12:09:37
    Template: False
     Deleted: False
```
