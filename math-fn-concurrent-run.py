import sys
from awsglue.utils import getResolvedOptions
import math

## @key_s: [TempDir, JOB_NAME]
args = getResolvedOptions(sys.argv,
                          ['JOB_NAME',
                           'key_1',
                           'key_2',
                           'key_3',
                           'key_4'])
     
                           
val_1 = math.sqrt(int(args['key_1']))
val_2 = math.sqrt(int(args['key_2']))
val_3 = math.sqrt(int(args['key_3']))
val_4 = math.sqrt(int(args['key_4']))

print('{}/{}/{}/{}'.format(val_1, val_2, val_3, val_4))
