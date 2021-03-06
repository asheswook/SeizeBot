from .default import *


class YTVideo:
    __slots__ = ['url', 'function_name', 'video_info', 'color1',
                 'color2', 'album_name', 'image_file']

    def __init__(self, url: str, function_name: str):
        self.url = url
        self.function_name = function_name

        defined_input = url.split('=')
        print(f'Load viewcount..... {defined_input[1]}')

        self.video_info = pafy.new(self.url)
        print('Success loading viewcount.')

    def get_views_int(self) -> int:  # int
        result = self.video_info.viewcount
        return result

    def get_views_str(self) -> str:  # str
        result = str(self.video_info.viewcount)
        return result

    def get_refined_views_str(self) -> str:  # refined viewcount (str)
        result = str(format(self.video_info.viewcount, ",d"))
        return result

    def get_comparison_views(self) -> int:  # int
        sql = "SELECT * FROM data WHERE name = '" + self.function_name + "'"
        cursor.execute(sql)
        db.commit()

        result = cursor.fetchall()

        try:
            result = result[0]['viewcount']

        except:
            print(self.function_name + "> row not found. create")
            sql = "INSERT INTO data (date, name, viewcount) VALUES ('0', '" + \
                self.function_name + "', 0)"
            cursor.execute(sql)
            db.commit()
            result = 0
            pass

        return result

    def get_views_increase(self) -> str:
        result = format(
            (self.get_views_int() - (self.get_comparison_views())), ",d")
        return result

    def get_wiki_content(self, color1, color2, album_name, image_file) -> str:
        result = """
||<|2><tablebordercolor=""" + color1 + """><width=100><""" + color1 + """>[[file:""" + image_file + """|width=100]]||<|1> '''""" + album_name + """''' ||
|| ์กฐํ์ """ + self.get_refined_views_str() + """ํ [br]{{{#green (+""" + self.get_views_increase() + """)}}} ||"""
        return result

    def update_database(self) -> None:
        date = str(dt.datetime.now())
        sql = "UPDATE data SET date='" + date + "', viewcount=" + \
            self.get_views_str() + " WHERE name='" + self.function_name + "'"
        cursor.execute(sql)
        db.commit()


def get_Vitaldata(specialComment="") -> str:
    viewIncrease = "0"
    data = ""
    date = str(dt.datetime.now())

    # Load ViewCounts

    FOLView = YTVideo(
        'https://www.youtube.com/watch?v=vPwaXytZcgI', 'FOL')
    TORView = YTVideo(
        'https://www.youtube.com/watch?v=XA2YEHn-A8Q', 'TOR')
    ICSView = YTVideo(
        'https://www.youtube.com/watch?v=CM4CkVFmTds', 'ICS')
    MNMView = YTVideo(
        'https://www.youtube.com/watch?v=mH0_XpSHkZo', 'MNM')
    FSView = YTVideo('https://www.youtube.com/watch?v=3ymwOvzhwHs', 'FS')
    FCView = YTVideo('https://www.youtube.com/watch?v=kOHB85vDuow', 'FC')
    OJJView = YTVideo(
        'https://www.youtube.com/watch?v=CfUGjK6gGgs', 'OJJ')
    YOYView = YTVideo(
        'https://www.youtube.com/watch?v=mAKsZ26SabQ', 'YOY')
    DNView = YTVideo(
        'https://www.youtube.com/watch?v=Fm5iP0S1z9w', 'DN')
    WILView = YTVideo(
        'https://www.youtube.com/watch?v=i0p1bmr0EmE', 'WIL')
    MNHView = YTVideo(
        'https://www.youtube.com/watch?v=zi_6oaQyckM', 'MNH')
    HSView = YTVideo('https://www.youtube.com/watch?v=rRzxEiBLQCA', 'HS')
    LKYView = YTVideo(
        'https://www.youtube.com/watch?v=V2hlQkVJZhE', 'LKY')
    TWSView = YTVideo(
        'https://www.youtube.com/watch?v=YdeeXDO--cs', 'TWS')
    SGNView = YTVideo(
        'https://www.youtube.com/watch?v=VQtonf1fv_s', 'SGN')
    KNKNView = YTVideo(
        'https://www.youtube.com/watch?v=8A2t_tAjMz8', 'KNKN')
    TTView = YTVideo(
        'https://www.youtube.com/watch?v=ePpPVE-GGJw', 'TT')
    CHEView = YTVideo(
        'https://www.youtube.com/watch?v=c7rCyll5AeY', 'CHE')
    OOHView = YTVideo(
        'https://www.youtube.com/watch?v=0rtV5esQT6I', 'OOH')

    # ์ผ๋ณธ์จ๋ฒ
    DGHView = YTVideo(
        'https://www.youtube.com/watch?v=VcOSUOpACq0', 'DGH')
    PFWView = YTVideo(
        'https://www.youtube.com/watch?v=fmOEKOjyDxU', 'PFW')
    KURView = YTVideo(
        'https://www.youtube.com/watch?v=BSS8Y-0hOlY', 'KUR')

    BTRView = YTVideo(
        'https://www.youtube.com/watch?v=sLmLwgxnPUE', 'BTR')
    FFRView = YTVideo(
        'https://www.youtube.com/watch?v=kRT174IdxuM', 'FFR')
    FNTView = YTVideo(
        'https://www.youtube.com/watch?v=zQELp93xxfo', 'FNT')
    BRTView = YTVideo(
        'https://www.youtube.com/watch?v=ZdKYi5ekshM', 'BRT')
    HPHPView = YTVideo(
        'https://www.youtube.com/watch?v=3n9rDwpa6QA', 'HPHP')
    BDZView = YTVideo(
        'https://www.youtube.com/watch?v=CMNahhgR_ss', 'BDZ')
    IWBView = YTVideo(
        'https://www.youtube.com/watch?v=X3H-4crGD6k', 'IWB')
    WMUView = YTVideo(
        'https://www.youtube.com/watch?v=DdLYSziSXII', 'WMU')
    CDPView = YTVideo(
        'https://www.youtube.com/watch?v=wQ_POfToaVY', 'CDP')
    OMTView = YTVideo(
        'https://www.youtube.com/watch?v=HuoOEry-Yc4', 'OMT')
    SBSView = YTVideo(
        'https://www.youtube.com/watch?v=96K5RxgTfW4', 'SBS')

    # ์์ด
    TFSView = YTVideo(
        'https://www.youtube.com/watch?v=f5_wn8mexmM', 'TFS')

    # ์ฑ๊ธ
    POPView = YTVideo('https://www.youtube.com/watch?v=f6YDKF0LVWw', 'POP')

    ######

    now = dt.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')  # ์๊ฐ ๊ฐฑ์?

    data += "Updated " + nowDatetime + "[br]" + specialComment

    data += FOLView.get_wiki_content("#003f9d", "#000000",
                                     "SCIENTIST", "FormulaofLoveAlbumCover.png")  # ์ฌ์ด์ธํฐ์คํธ
    data += TORView.get_wiki_content("#003f9d", "#000000",
                                     "Alcohol-Free", "TasteofLoveAlbumCover.jpeg")  # ํ์ค๋ฝ
    data += ICSView.get_wiki_content("#a01623", "#000000",
                                     "I CAN'T STOP ME", "The2ndFullAlbumCover.jpeg")  # ์์บ์ค
    data += MNMView.get_wiki_content("#F8F8F0", "#CCA050",
                                     "MORE & MORE", "MORENMOREAlbumCover.jpg")  # More & More
    data += FSView.get_wiki_content("#000000", "#D3C15E",
                                    "Feel Special", "FeelSpecialAlbumCover.jpg")  # ํ์ค
    data += FCView.get_wiki_content("#8FE1EF", "#FF45A0",
                                    "FANCY YOU", "FancyYouAlbumCover.jpg")  # Fancy
    data += OJJView.get_wiki_content("#981419", "#D5B46E",
                                     "์ฌํด ์?์ผ ์ํ ์ผ", "TheyearofYESAlbumCover.jpg")  # ์ฌ์?์
    data += YOYView.get_wiki_content("#000000", "#D61617",
                                     "YES or YES", "YESorYESAlbumCover.jpg")  # YES or YES
    data += DNView.get_wiki_content("#041F56", "#D5B956", "Dance The Night Away",
                                    "SummerNightsAlbumCover.jpg")  # Dance The Night Away
    data += WILView.get_wiki_content("#FABDC5", "#C30D00",
                                     "What is Love?", "WhatisLoveAlbumCover.jpg")  # ์์ด์ฆ๋ฝ
    data += MNHView.get_wiki_content("#007A4B", "#E6BE8A",
                                     "Merry & Happy", "MerryHappyAlbumCover.jpg")  # ๋ฉ๋ฆฌํดํผ_1
    data += HSView.get_wiki_content("#007A4B", "#E6BE8A",
                                    "Heart Shaker", "MerryHappyAlbumCover.jpg")  # ๋ฉ๋ฆฌํดํผ_2
    data += LKYView.get_wiki_content("#F5B0CD", "#2F79C1",
                                     "LIKEY", "TwicetagramAlbumCover.jpg")  # LIKEY
    data += SGNView.get_wiki_content("#001F46", "#FF3366",
                                     "SIGNAL", "SIGNALAlbumCover.jpg")  # SIGNAL
    data += KNKNView.get_wiki_content("#FF6633", "#FEE238", "KNOCK KNOCK",
                                      "TWICEcoasterLANE2AlbumCover.jpg")  # KNOCK KNOCK
    data += TTView.get_wiki_content("#FF5FA2", "#FCC89B",
                                    "TT", "TWICEcoasterLANE1AlbumCover.jpg")  # TT
    data += CHEView.get_wiki_content("#40D8CC", "#FFFFFF",
                                     "CHEER UP", "PAGETWOAlbumCover.jpg")  # CHEER UP
    data += OOHView.get_wiki_content("#EB0F66", "#FFFFFF",
                                     "OOH-AHHํ๊ฒ", "THESTORYBEGINSAlbumCover.jpg")  # OOH-AHHํ๊ฒ
    data += TWSView.get_wiki_content("#000000", "#FFFFFF",
                                     "ํธ์์ด์ค์ก", "TWICESongCover.png")  # ํธ์์ด์ค์ก
    data += """
----
{{{+1 '''Japan Albums'''}}}

"""
    data += DGHView.get_wiki_content("#000000", "#FFFFFF",
                                     "Doughnut", "DoughnutAlbumCover.jpg")  # Doughnut
    data += PFWView.get_wiki_content("#d8a45a", "#FFFFFF", "Perfect World",
                                     "PerfectWorldAlbumCover.jpeg")  # Perfect World
    data += KURView.get_wiki_content("#000000", "#FFFFFF",
                                     "Kura Kura", "KuraKuraAlbumCover.jpg")  # KURA-KURA
    data += BTRView.get_wiki_content("#000000", "#FFFFFF",
                                     "BETTER", "BETTERAlbumCover.jpg")  # BETTER
    data += FFRView.get_wiki_content("#000000", "#FFFFFF",
                                     "FanFare", "FanFareAlbumCover.jpg")  # FANFARE
    data += FNTView.get_wiki_content("#000000", "#FFFFFF",
                                     "Fake & True", "FakeNTrueAlbumCover.jpg")  # Fake and True
    data += BRTView.get_wiki_content("#000000", "#FFFFFF", "Breakthrough",
                                     "BreakthroughAlbumCover.jpg")  # Breakthrough
    data += HPHPView.get_wiki_content("#000000", "#FFFFFF",
                                      "HAPPY HAPPY", "HAPPYHAPPYAlbumCover.jpg")  # HAPPY HAPPY
    data += IWBView.get_wiki_content("#000000", "#FFFFFF", "I WANT YOU BACK",
                                     "IWANTYOUBACKAlbumCover.jpg")  # I WANT YOU BACK
    data += SBSView.get_wiki_content("#000000", "#ffffff", "STAY BY MY SIDE",
                                     "STAYBYMYALBUMCOVER.jpg")  # Stay by my side
    data += BDZView.get_wiki_content("#000000",
                                     "#FFFFFF", "BDZ", "BDZAlbumCover.jpg")  # BDZ
    data += WMUView.get_wiki_content("#000000", "#FFFFFF",
                                     "Wake Me Up", "WakeMeUpAlbumCover.jpg")  # Wake Me Up
    data += CDPView.get_wiki_content("#000000", "#FFFFFF",
                                     "Candy Pop", "CandyPopAlbumCover.jpg")  # Candy Pop
    data += OMTView.get_wiki_content("#000000", "#FFFFFF", "One More Time",
                                     "OneMoreTimeAlbumCover.jpg")  # One More Time

    data += """
----
{{{+1 '''English Albums'''}}}

"""
    data += TFSView.get_wiki_content("#ff669e", "#fee6f2",
                                     "The Feels", "TheFeelsAlbumCover.jpeg")  # The feels

    data += """
----
{{{+1 '''Single Albums'''}}}

"""
    data += POPView.get_wiki_content("#f7f48d", "#FFFFFF",
                                     "POP!", "NayeonPOPAlbumCover.jpeg")  # Nayeon POP!

    # Update Database
    print("update database")
    FOLView.update_database()
    TORView.update_database()
    ICSView.update_database()
    MNMView.update_database()
    FSView.update_database()
    FCView.update_database()
    OJJView.update_database()
    YOYView.update_database()
    DNView.update_database()
    WILView.update_database()
    MNHView.update_database()
    HSView.update_database()
    LKYView.update_database()
    TWSView.update_database()
    SGNView.update_database()
    KNKNView.update_database()
    TTView.update_database()
    CHEView.update_database()
    OOHView.update_database()

    # ์ผ๋ณธ์จ๋ฒ
    DGHView.update_database()
    KURView.update_database()
    PFWView.update_database()
    BTRView.update_database()
    FFRView.update_database()
    FNTView.update_database()
    BRTView.update_database()
    HPHPView.update_database()
    BDZView.update_database()
    IWBView.update_database()
    WMUView.update_database()
    CDPView.update_database()
    OMTView.update_database()
    SBSView.update_database()

    # ์์ด
    TFSView.update_database()

    # ์ฑ๊ธ
    POPView.update_database()
    print("ok")
    return data
