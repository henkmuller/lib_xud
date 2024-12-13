is_io = {}
uses_memory = {}
may_go_on = {}
is_io['add'] = False
is_io['and'] = False
is_io['bau'] = False
is_io['bf'] = False
is_io['bl'] = False
is_io['bru'] = False
is_io['bt'] = False
is_io['bu'] = False
is_io['buwc'] = False
is_io['clre'] = False
is_io['clrpt'] = False
is_io['clrsr'] = False
is_io['crc32'] = False
is_io['crc32_inc'] = False
is_io['crc8'] = False
is_io['crcn'] = False
is_io['dualentsp'] = False
is_io['ecallf'] = False
is_io['eeu'] = False
is_io['edu'] = False
is_io['endin'] = False
is_io['eq'] = False
is_io['freer'] = False
is_io['getr'] = False
is_io['getts'] = False
is_io['in'] = True
is_io['inpw'] = True
is_io['ld8u'] = False
is_io['ldap'] = False
is_io['ldaw'] = False
is_io['ldc'] = False
is_io['ldw'] = False
is_io['mkmsk'] = False
is_io['nop'] = False
is_io['not'] = False
is_io['out'] = True
is_io['outct'] = False
is_io['outpw'] = True
is_io['outt'] = False
is_io['retsp'] = False
is_io['setc'] = False
is_io['setd'] = False
is_io['setpsc'] = False
is_io['setpt'] = False
is_io['setsr'] = False
is_io['setv'] = False
is_io['shr'] = False
is_io['stw'] = False
is_io['sub'] = False
is_io['syncr'] = False
is_io['waiteu'] = False
is_io['xor'] = False
is_io['fnop'] = False

uses_memory['add'] = False
uses_memory['and'] = False
uses_memory['bau'] = False
uses_memory['bf'] = False
uses_memory['bl'] = False
uses_memory['bru'] = False
uses_memory['bt'] = False
uses_memory['bu'] = False
uses_memory['buwc'] = False
uses_memory['clre'] = False
uses_memory['clrpt'] = False
uses_memory['clrsr'] = False
uses_memory['crc32'] = False
uses_memory['crc32_inc'] = False
uses_memory['crc8'] = False
uses_memory['crcn'] = False
uses_memory['dualentsp'] = True
uses_memory['ecallf'] = False
uses_memory['eeu'] = False
uses_memory['edu'] = False
uses_memory['endin'] = False
uses_memory['eq'] = False
uses_memory['freer'] = False
uses_memory['getr'] = False
uses_memory['getts'] = False
uses_memory['in'] = False
uses_memory['inpw'] = False
uses_memory['ld8u'] = True
uses_memory['ldap'] = False
uses_memory['ldaw'] = False
uses_memory['ldc'] = False
uses_memory['ldw'] = True
uses_memory['mkmsk'] = False
uses_memory['nop'] = False
uses_memory['not'] = False
uses_memory['out'] = False
uses_memory['outct'] = False
uses_memory['outpw'] = False
uses_memory['outt'] = False
uses_memory['retsp'] = False
uses_memory['setc'] = False
uses_memory['setd'] = False
uses_memory['setpsc'] = False
uses_memory['setpt'] = False
uses_memory['setsr'] = False
uses_memory['setv'] = False
uses_memory['shr'] = False
uses_memory['stw'] = True
uses_memory['sub'] = False
uses_memory['syncr'] = False
uses_memory['waiteu'] = False
uses_memory['xor'] = False
uses_memory['fnop'] = True

may_go_on['add'] = True
may_go_on['and'] = True
may_go_on['bau'] = False
may_go_on['bf'] = True
may_go_on['bl'] = False
may_go_on['bru'] = False
may_go_on['bt'] = True
may_go_on['bu'] = False
may_go_on['buwc'] = False
may_go_on['clre'] = True
may_go_on['clrpt'] = True
may_go_on['clrsr'] = True
may_go_on['crc32'] = True
may_go_on['crc32_inc'] = True
may_go_on['crc8'] = True
may_go_on['crcn'] = True
may_go_on['dualentsp'] = True
may_go_on['ecallf'] = True
may_go_on['eeu'] = True
may_go_on['edu'] = True
may_go_on['endin'] = True
may_go_on['eq'] = True
may_go_on['freer'] = True
may_go_on['getr'] = True
may_go_on['getts'] = True
may_go_on['in'] = True
may_go_on['inpw'] = True
may_go_on['ld8u'] = True
may_go_on['ldap'] = True
may_go_on['ldaw'] = True
may_go_on['ldc'] = True
may_go_on['ldw'] = True
may_go_on['mkmsk'] = True
may_go_on['nop'] = True
may_go_on['not'] = True
may_go_on['out'] = True
may_go_on['outct'] = True
may_go_on['outpw'] = True
may_go_on['outt'] = True
may_go_on['retsp'] = False
may_go_on['setc'] = True
may_go_on['setd'] = True
may_go_on['setpsc'] = True
may_go_on['setpt'] = True
may_go_on['setsr'] = True
may_go_on['setv'] = True
may_go_on['shr'] = True
may_go_on['stw'] = True
may_go_on['sub'] = True
may_go_on['syncr'] = True
may_go_on['waiteu'] = False
may_go_on['xor'] = True
may_go_on['fnop'] = True
