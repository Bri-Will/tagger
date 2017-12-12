IP_PATTERN_LIST = [
    [{'SHAPE':'d.d.d.d'}],
    [{'SHAPE':'d.d.d.dd'}],
    [{'SHAPE':'d.d.d.ddd'}],
    [{'SHAPE':'d.d.dd.d'}],
    [{'SHAPE':'d.d.dd.dd'}],
    [{'SHAPE':'d.d.dd.ddd'}],
    [{'SHAPE':'d.d.ddd.d'}],
    [{'SHAPE':'d.d.ddd.dd'}],
    [{'SHAPE':'d.d.ddd.ddd'}],
    [{'SHAPE':'d.dd.d.d'}],
    [{'SHAPE':'d.dd.d.dd'}],
    [{'SHAPE':'d.dd.d.ddd'}],
    [{'SHAPE':'d.dd.dd.d'}],
    [{'SHAPE':'d.dd.dd.dd'}],
    [{'SHAPE':'d.dd.dd.ddd'}],
    [{'SHAPE':'d.dd.ddd.d'}],
    [{'SHAPE':'d.dd.ddd.dd'}],
    [{'SHAPE':'d.dd.ddd.ddd'}],
    [{'SHAPE':'d.ddd.d.d'}],
    [{'SHAPE':'d.ddd.d.dd'}],
    [{'SHAPE':'d.ddd.d.ddd'}],
    [{'SHAPE':'d.ddd.dd.d'}],
    [{'SHAPE':'d.ddd.dd.dd'}],
    [{'SHAPE':'d.ddd.dd.ddd'}],
    [{'SHAPE':'d.ddd.ddd.d'}],
    [{'SHAPE':'d.ddd.ddd.dd'}],
    [{'SHAPE':'d.ddd.ddd.ddd'}],
    [{'SHAPE':'dd.d.d.d'}],
    [{'SHAPE':'dd.d.d.dd'}],
    [{'SHAPE':'dd.d.d.ddd'}],
    [{'SHAPE':'dd.d.dd.d'}],
    [{'SHAPE':'dd.d.dd.dd'}],
    [{'SHAPE':'dd.d.dd.ddd'}],
    [{'SHAPE':'dd.d.ddd.d'}],
    [{'SHAPE':'dd.d.ddd.dd'}],
    [{'SHAPE':'dd.d.ddd.ddd'}],
    [{'SHAPE':'dd.dd.d.d'}],
    [{'SHAPE':'dd.dd.d.dd'}],
    [{'SHAPE':'dd.dd.d.ddd'}],
    [{'SHAPE':'dd.dd.dd.d'}],
    [{'SHAPE':'dd.dd.dd.dd'}],
    [{'SHAPE':'dd.dd.dd.ddd'}],
    [{'SHAPE':'dd.dd.ddd.d'}],
    [{'SHAPE':'dd.dd.ddd.dd'}],
    [{'SHAPE':'dd.dd.ddd.ddd'}],
    [{'SHAPE':'dd.ddd.d.d'}],
    [{'SHAPE':'dd.ddd.d.dd'}],
    [{'SHAPE':'dd.ddd.d.ddd'}],
    [{'SHAPE':'dd.ddd.dd.d'}],
    [{'SHAPE':'dd.ddd.dd.dd'}],
    [{'SHAPE':'dd.ddd.dd.ddd'}],
    [{'SHAPE':'dd.ddd.ddd.d'}],
    [{'SHAPE':'dd.ddd.ddd.dd'}],
    [{'SHAPE':'dd.ddd.ddd.ddd'}],
    [{'SHAPE':'ddd.d.d.d'}],
    [{'SHAPE':'ddd.d.d.dd'}],
    [{'SHAPE':'ddd.d.d.ddd'}],
    [{'SHAPE':'ddd.d.dd.d'}],
    [{'SHAPE':'ddd.d.dd.dd'}],
    [{'SHAPE':'ddd.d.dd.ddd'}],
    [{'SHAPE':'ddd.d.ddd.d'}],
    [{'SHAPE':'ddd.d.ddd.dd'}],
    [{'SHAPE':'ddd.d.ddd.ddd'}],
    [{'SHAPE':'ddd.dd.d.d'}],
    [{'SHAPE':'ddd.dd.d.dd'}],
    [{'SHAPE':'ddd.dd.d.ddd'}],
    [{'SHAPE':'ddd.dd.dd.d'}],
    [{'SHAPE':'ddd.dd.dd.dd'}],
    [{'SHAPE':'ddd.dd.dd.ddd'}],
    [{'SHAPE':'ddd.dd.ddd.d'}],
    [{'SHAPE':'ddd.dd.ddd.dd'}],
    [{'SHAPE':'ddd.dd.ddd.ddd'}],
    [{'SHAPE':'ddd.ddd.d.d'}],
    [{'SHAPE':'ddd.ddd.d.dd'}],
    [{'SHAPE':'ddd.ddd.d.ddd'}],
    [{'SHAPE':'ddd.ddd.dd.d'}],
    [{'SHAPE':'ddd.ddd.dd.dd'}],
    [{'SHAPE':'ddd.ddd.dd.ddd'}],
    [{'SHAPE':'ddd.ddd.ddd.d'}],
    [{'SHAPE':'ddd.ddd.ddd.dd'}],
    [{'SHAPE':'ddd.ddd.ddd.ddd'}]
    ]

TWITTER_PATTERN_LIST = [
    [{'SHAPE':'@XxxxxXxxxx'}],
    [{'SHAPE':'@xxxx'}],
    [{'SHAPE':'@XXXX'}],
    [{'SHAPE':'@Xxxxx'}]
    ]

ADDRESS_PATTERN_LIST = [
    [{'LIKE_NUM':True}, {'SHAPE':'Xxxxx'}, {'SHAPE':'Xx'}, {'IS_PUNCT':True}, {'ENT_TYPE':'GPE'}, {'IS_PUNCT':True}, {'ENT_TYPE':'GPE'}, {'LIKE_NUM': True}],
    [{'LIKE_NUM':True}, {'SHAPE':'Xxxxx'}, {'SHAPE':'Xx.'}, {'IS_PUNCT':True}, {'ENT_TYPE':'GPE'}, {'IS_PUNCT':True}, {'ENT_TYPE':'GPE'}, {'LIKE_NUM': True}],
    [{'LIKE_NUM':True}, {'SHAPE':'Xxxxx'}, {'SHAPE':'Xx'}, {'IS_PUNCT':True}, {'ENT_TYPE':'GPE'}, {'IS_PUNCT':True}, {'SHAPE':'XX'}, {'LIKE_NUM': True}],
    [{'LIKE_NUM':True}, {'SHAPE':'Xxxxx'}, {'SHAPE':'Xx.'}, {'IS_PUNCT':True}, {'ENT_TYPE':'GPE'}, {'IS_PUNCT':True}, {'SHAPE':'XX'}, {'LIKE_NUM': True}]
    ]

PHONE_PATTERN_LIST = [
    #Format: AAAA-BBBB
    [{'LIKE_NUM':True}, {'ORTH':'-', 'OP':'?'}, {'LIKE_NUM':True}],

    #Format: AA BB CC
    [{'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}],

    #Format: AA BB CC DD
    [{'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}],

    #Format: (AAAA) BBBB
    [{'ORTH':'('}, {'LIKE_NUM':True}, {'ORTH':')'}, {'LIKE_NUM':True}],

    #Format: +CountryCode AAAA BBBB
    [{'ORTH':'+'}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}],

    #NADP (North America Numbering Plan)
    [{'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'dddd'}],
    [{'ORTH':'1'}, {'ORTH':'-'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'dddd'}],
    [{'ORTH':'+'}, {'ORTH':'1'}, {'ORTH':'-'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'dddd'}],
    [{'ORTH':'1'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'dddd'}],
    [{'ORTH':'('}, {'SHAPE':'ddd'}, {'ORTH':')'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'dddd'}],
    [{'ORTH':'+'}, {'ORTH':'1'}, {'ORTH':'('}, {'SHAPE':'ddd'}, {'ORTH':')'}, {'SHAPE':'ddd'}, {'ORTH':'-'}, {'SHAPE':'dddd'}],

    #Format: +CountryCode (AAAA) BBBB
    [{'ORTH':'+'}, {'LIKE_NUM':True}, {'ORTH':'('}, {'LIKE_NUM':True}, {'ORTH':')'}, {'LIKE_NUM':True}],

    #Format: +CountryCode AA BB CC DD
    [{'ORTH':'+'}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}],

    #Format: +CountryCode AAAA-BBBB
    [{'ORTH':'+'}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'ORTH':'-'}, {'LIKE_NUM':True}],

    #Format: (AAAA) BBBB CCCC
    [{'ORTH':'('}, {'LIKE_NUM':True}, {'ORTH':')'}, {'LIKE_NUM':True}, {'LIKE_NUM':True}],

    #Format: (AAAA) BBBB-CCCC
    [{'ORTH':'('}, {'LIKE_NUM':True}, {'ORTH':')'}, {'LIKE_NUM':True}, {'ORTH':'-'}, {'LIKE_NUM':True}],

    #Format: AA BB CC DD
    [{'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}],

    #Format: +CountryCode AA BB CC DD
    [{'ORTH':'+'}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}, {'LIKE_NUM':True}],

    #Format: AA BB CC DD EE
    [{'SHAPE':'dd'}, {'SHAPE':'dd'}, {'SHAPE':'dd'}, {'SHAPE':'dd'}, {'SHAPE':'dd'}],

    #Format: +CountryCode AA BB CC DD EE
    [{'ORTH':'+'}, {'LIKE_NUM':True}, {'SHAPE':'dd'}, {'SHAPE':'dd'}, {'SHAPE':'dd'}, {'SHAPE':'dd'}, {'SHAPE':'dd'}]

    ]
