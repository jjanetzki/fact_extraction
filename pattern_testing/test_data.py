def test_articles_list():
    return [
        (
            'While living in <a href="/wiki/Annapolis,_Maryland" title="Annapolis, Maryland">Annapolis</a> with her husband and their four children , Agnew served as the president of her local <a href="/wiki/Parent-Teacher_Association" title="Parent-Teacher Association">PTA</a> , and volunteered as both an assistant <a href="/wiki/Girl_Scouts_of_the_USA" title="Girl Scouts of the USA">Girl Scout</a> troop leader and a board member of the <a href="/wiki/Kiwanis" title="Kiwanis">Kiwanis Club</a> womens auxiliary .',
            'Judy_Agnew',
            []),
        (
            'He recently became a professor at the <a href="/wiki/Massachusetts_Institute_of_Technology">MIT</a>.',
            'John_Doe',
            [('John_Doe', 'http://dbpedia.org/ontology/almaMater',
              'http://dbpedia.org/resource/Massachusetts_Institute_of_Technology')]),
        (
            'She really loves <a href="/wiki/Pyrotechnics">pyrotechnics</a>.',
            'Jane_Doe',
            []),
        (
            'Some person was born in <a href="/wiki/Braunschweig">Braunschweig</a>.',
            'Not me',
            [('Not me', 'http://dbpedia.org/ontology/birthPlace',
              'http://dbpedia.org/resource/Braunschweig')]),
        (
            'Merkel was educated in Templin and at the <a href="/wiki/University_of_Leipzig">University of Leipzig</a>, where she studied <a href="/wiki/Physics">physics</a> from 1973 to 1978.',
            'Angela_Merkel',
            [('Angela_Merkel', 'http://dbpedia.org/ontology/almaMater',
              'http://dbpedia.org/resource/University_of_Leipzig')]),
        (
            'Irma Raush was born in <a href="/wiki/Saratov">Saratov</a> on 21 April 1938 into a Volga German family.',
            'Irma_Raush',
            [('Irma_Raush', 'http://dbpedia.org/ontology/birthPlace',
              'http://dbpedia.org/resource/Saratov')]),
        (
            'Born Elinor Isabel Judefind in <a href="/wiki/Baltimore">Baltimore, Maryland</a> , to parents of French-German descent , Agnew was daughter of William Lee Judefind , a <a href="/wiki/Chemist">chemist</a> , and his wife , the former Ruth Elinor Schafer . ',
            'Judy_Agnew',
            [('Judy_Agnew', 'http://dbpedia.org/ontology/birthPlace',
              'http://dbpedia.org/resource/Baltimore')]),
        (
            'Her paternal grandfather was a <a href="/wiki/Methodism">Methodist</a> minister .',
            'Judy_Agnew',
            [])
        # (
        #     '',
        #     '',
        #     [])
    ]
