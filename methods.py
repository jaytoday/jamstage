
API_LIST = 			    [

          {
            'name': 'code',
            'description': '',
            'methods': [
              {
               'name': 'code.get',
               'description': 'Get media and information associated with a code',
                'collection': 'media',
                'query': 'codeid=1&codepw=[password]&[quiet=true]&skip=[skip]&limit=[limit]&mm=[generated hash]'
              },
             {
               'name': 'code.update',
               'description': 'Update properties of a code',
                 'query': 'codeid=1400300831950&codepw=11e676cb692eb54d0e55b171198b30ed&authuname=billy&authpw=11e676cb692eb54d0e55b171198b30ed&password=testing&title=test%20stickybit%20sticker'
             
              },
              {
               'name': 'code.popular',
               'description': 'Get a list of codes sorted by popularity',
               'collection': 'codes',
               'query': 'skip=[skip]&limit=[limit]&since=[since]&mm=[generated hash]',
             }
            ]
			    },
			    {
            'name': 'user',
            'description': '',
            'methods': [
              {
               'name': 'user.info',
               'description': 'Get information about a user',
               'query': 'username=billy&mm=[generated hash]',
              },
                            {
               'name': 'user.bits',
               'description': 'Get the bits attached by a user',
               'query': 'username=billy&skip=[skip]&limit=[limit]&mm=[generated hash]',
               'collection': 'bits'
              },
             {
               'name': 'user.find',
               'description': 'Find friends for a  user',
               'query': 'authuname=billy&authpw=11e676cb692eb54d0e55b171198b30ed&search=joe&mm=[generated hash]',
              }
            ]
			    },
          {
            'name': 'social',
            'description': '',
            'methods': [
              {
               'name': 'social.venues',
               'description': 'Get nearby venues',
               'query': 'lat=[lat]&long=[long]&q=[search]&l=[limit]&mm=[generated hash]',
              }
            ]
			    },
          {
            'name': 'notify',
            'description': '',
            'methods': [
              {
               'name': 'notify.set',
               'description': 'Add or remove a notifier'
              },
             {
               'name': 'notify.get',
               'description': 'Get notifications for a code'
              }
            ]
			    }
			    ]
