from main import PrismstoneSpider


def split_id_and_name(id_and_name, expected_id, expected_name):
    spider = PrismstoneSpider()
    id, name = spider._split_id_and_name(id_and_name)
    assert id == expected_id
    assert name == expected_name


def test_split_id_and_name_1():
    id_and_name = 'AS-09-050 セクシーパールネックレス'
    id = 'AS-09-050'
    name = 'セクシーパールネックレス'
    split_id_and_name(id_and_name, id, name)


def test_split_id_and_name_2():
    id_and_name = 'AS-SHI04★ かがやきのシンフォニア\u3000ネックレス'
    id = 'AS-SHI04★'
    name = 'かがやきのシンフォニア ネックレス'
    split_id_and_name(id_and_name, id, name)


def test_split_id_and_name_3():
    id_and_name = 'AS-S10★ きぐるみ\u3000ラビットさん'
    id = 'AS-S10★'
    name = 'きぐるみ ラビットさん'
    split_id_and_name(id_and_name, id, name)


def test_split_id_and_name_4():
    id_and_name = 'AS-S10★きぐるみ\u3000ラビットさん'
    id = 'AS-S10★'
    name = 'きぐるみ ラビットさん'
    split_id_and_name(id_and_name, id, name)

