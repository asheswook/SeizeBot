from .default import *


class loadViewCount:
    def __init__(self, urlInput, functionName):
        self.url = urlInput
        self.functionName = functionName
        definedInput = urlInput.split('=')
        print(f'Load viewcount..... {definedInput[1]}')
        self.video_info = pafy.new(self.url)
        print('Success loading viewcount.')

    def getViewCountInt(self):  # int
        result = self.video_info.viewcount
        return result

    def getViewCountStr(self):  # str
        result = str(self.video_info.viewcount)
        return result

    def getRefinedViewCount(self):  # refined viewcount (str)
        result = str(format(self.video_info.viewcount, ",d"))
        return result

    def getComparedCountRAW(self):  # int
        sql = "SELECT * FROM data WHERE name = '" + self.functionName + "'"
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        try:
            result = result[0]['viewcount']

        except:
            print(self.functionName + "> row not found. create")
            sql = "INSERT INTO data (date, name, viewcount) VALUES ('0', '" + \
                self.functionName + "', 0)"
            cursor.execute(sql)
            db.commit()
            result = 0
            pass

        return result

    def getViewIncrease(self):
        result = format(
            (self.getViewCountInt() - (self.getComparedCountRAW())), ",d")
        return result

    def getWikiContent(self, color1, color2, album_name, image_file):
        result = """
||<|2><tablebordercolor=""" + color1 + """><width=100><""" + color1 + """>[[file:""" + image_file + """|width=100]]||<|1> '''""" + album_name + """''' ||
|| 조회수 """ + self.getRefinedViewCount() + """회 [br]{{{#green (+""" + self.getViewIncrease() + """)}}} ||"""
        return result

    def updateDatabase(self):
        date = str(dt.datetime.now())
        sql = "UPDATE data SET date='" + date + "', viewcount=" + \
            self.getViewCountStr() + " WHERE name='" + self.functionName + "'"
        cursor.execute(sql)
        db.commit()


def updateDB(specialComment=""):
    viewIncrease = "0"
    data = ""
    date = str(dt.datetime.now())

    # Load ViewCounts

    FOLView = loadViewCount(
        'https://www.youtube.com/watch?v=vPwaXytZcgI', 'FOL')
    TORView = loadViewCount(
        'https://www.youtube.com/watch?v=XA2YEHn-A8Q', 'TOR')
    ICSView = loadViewCount(
        'https://www.youtube.com/watch?v=CM4CkVFmTds', 'ICS')
    MNMView = loadViewCount(
        'https://www.youtube.com/watch?v=mH0_XpSHkZo', 'MNM')
    FSView = loadViewCount('https://www.youtube.com/watch?v=3ymwOvzhwHs', 'FS')
    FCView = loadViewCount('https://www.youtube.com/watch?v=kOHB85vDuow', 'FC')
    OJJView = loadViewCount(
        'https://www.youtube.com/watch?v=CfUGjK6gGgs', 'OJJ')
    YOYView = loadViewCount(
        'https://www.youtube.com/watch?v=mAKsZ26SabQ', 'YOY')
    DNView = loadViewCount(
        'https://www.youtube.com/watch?v=Fm5iP0S1z9w', 'DN')
    WILView = loadViewCount(
        'https://www.youtube.com/watch?v=i0p1bmr0EmE', 'WIL')
    MNHView = loadViewCount(
        'https://www.youtube.com/watch?v=zi_6oaQyckM', 'MNH')
    HSView = loadViewCount('https://www.youtube.com/watch?v=rRzxEiBLQCA', 'HS')
    LKYView = loadViewCount(
        'https://www.youtube.com/watch?v=V2hlQkVJZhE', 'LKY')
    TWSView = loadViewCount(
        'https://www.youtube.com/watch?v=YdeeXDO--cs', 'TWS')
    SGNView = loadViewCount(
        'https://www.youtube.com/watch?v=VQtonf1fv_s', 'SGN')
    KNKNView = loadViewCount(
        'https://www.youtube.com/watch?v=8A2t_tAjMz8', 'KNKN')
    TTView = loadViewCount(
        'https://www.youtube.com/watch?v=ePpPVE-GGJw', 'TT')
    CHEView = loadViewCount(
        'https://www.youtube.com/watch?v=c7rCyll5AeY', 'CHE')
    OOHView = loadViewCount(
        'https://www.youtube.com/watch?v=0rtV5esQT6I', 'OOH')

    # 일본앨범
    DGHView = loadViewCount(
        'https://www.youtube.com/watch?v=VcOSUOpACq0', 'DGH')
    PFWView = loadViewCount(
        'https://www.youtube.com/watch?v=fmOEKOjyDxU', 'PFW')
    KURView = loadViewCount(
        'https://www.youtube.com/watch?v=BSS8Y-0hOlY', 'KUR')

    BTRView = loadViewCount(
        'https://www.youtube.com/watch?v=sLmLwgxnPUE', 'BTR')
    FFRView = loadViewCount(
        'https://www.youtube.com/watch?v=kRT174IdxuM', 'FFR')
    FNTView = loadViewCount(
        'https://www.youtube.com/watch?v=zQELp93xxfo', 'FNT')
    BRTView = loadViewCount(
        'https://www.youtube.com/watch?v=ZdKYi5ekshM', 'BRT')
    HPHPView = loadViewCount(
        'https://www.youtube.com/watch?v=3n9rDwpa6QA', 'HPHP')
    BDZView = loadViewCount(
        'https://www.youtube.com/watch?v=CMNahhgR_ss', 'BDZ')
    IWBView = loadViewCount(
        'https://www.youtube.com/watch?v=X3H-4crGD6k', 'IWB')
    WMUView = loadViewCount(
        'https://www.youtube.com/watch?v=DdLYSziSXII', 'WMU')
    CDPView = loadViewCount(
        'https://www.youtube.com/watch?v=wQ_POfToaVY', 'CDP')
    OMTView = loadViewCount(
        'https://www.youtube.com/watch?v=HuoOEry-Yc4', 'OMT')
    SBSView = loadViewCount(
        'https://www.youtube.com/watch?v=96K5RxgTfW4', 'SBS')

    # 영어
    TFSView = loadViewCount(
        'https://www.youtube.com/watch?v=f5_wn8mexmM', 'TFS')

    ######

    now = dt.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')  # 시간 갱신

    data += "Updated " + nowDatetime + "[br]" + specialComment

    data += FOLView.getWikiContent("#003f9d", "#000000",
                                   "SCIENTIST", "FormulaofLoveAlbumCover.png")  # 사이언티스트
    data += TORView.getWikiContent("#003f9d", "#000000",
                                   "Alcohol-Free", "TasteofLoveAlbumCover.jpeg")  # 테오럽
    data += ICSView.getWikiContent("#a01623", "#000000",
                                   "I CAN'T STOP ME", "The2ndFullAlbumCover.jpeg")  # 아캔스
    data += MNMView.getWikiContent("#F8F8F0", "#CCA050",
                                   "MORE & MORE", "MORENMOREAlbumCover.jpg")  # More & More
    data += FSView.getWikiContent("#000000", "#D3C15E",
                                  "Feel Special", "FeelSpecialAlbumCover.jpg")  # 필스
    data += FCView.getWikiContent("#8FE1EF", "#FF45A0",
                                  "FANCY YOU", "FancyYouAlbumCover.jpg")  # Fancy
    data += OJJView.getWikiContent("#981419", "#D5B46E",
                                   "올해 제일 잘한 일", "TheyearofYESAlbumCover.jpg")  # 올제잘
    data += YOYView.getWikiContent("#000000", "#D61617",
                                   "YES or YES", "YESorYESAlbumCover.jpg")  # YES or YES
    data += DNView.getWikiContent("#041F56", "#D5B956", "Dance The Night Away",
                                  "SummerNightsAlbumCover.jpg")  # Dance The Night Away
    data += WILView.getWikiContent("#FABDC5", "#C30D00",
                                   "What is Love?", "WhatisLoveAlbumCover.jpg")  # 왓이즈럽
    data += MNHView.getWikiContent("#007A4B", "#E6BE8A",
                                   "Merry & Happy", "MerryHappyAlbumCover.jpg")  # 메리해피_1
    data += HSView.getWikiContent("#007A4B", "#E6BE8A",
                                  "Heart Shaker", "MerryHappyAlbumCover.jpg")  # 메리해피_2
    data += LKYView.getWikiContent("#F5B0CD", "#2F79C1",
                                   "LIKEY", "TwicetagramAlbumCover.jpg")  # LIKEY
    data += SGNView.getWikiContent("#001F46", "#FF3366",
                                   "SIGNAL", "SIGNALAlbumCover.jpg")  # SIGNAL
    data += KNKNView.getWikiContent("#FF6633", "#FEE238", "KNOCK KNOCK",
                                    "TWICEcoasterLANE2AlbumCover.jpg")  # KNOCK KNOCK
    data += TTView.getWikiContent("#FF5FA2", "#FCC89B",
                                  "TT", "TWICEcoasterLANE1AlbumCover.jpg")  # TT
    data += CHEView.getWikiContent("#40D8CC", "#FFFFFF",
                                   "CHEER UP", "PAGETWOAlbumCover.jpg")  # CHEER UP
    data += OOHView.getWikiContent("#EB0F66", "#FFFFFF",
                                   "OOH-AHH하게", "THESTORYBEGINSAlbumCover.jpg")  # OOH-AHH하게
    data += TWSView.getWikiContent("#000000", "#FFFFFF",
                                   "트와이스송", "TWICESongCover.png")  # 트와이스송
    data += """
----
{{{+1 '''Japan Albums'''}}}

"""
    data += DGHView.getWikiContent("#000000", "#FFFFFF",
                                   "Doughnut", "DoughnutAlbumCover.jpg")  # Doughnut
    data += PFWView.getWikiContent("#d8a45a", "#FFFFFF", "Perfect World",
                                   "PerfectWorldAlbumCover.jpeg")  # Perfect World
    data += KURView.getWikiContent("#000000", "#FFFFFF",
                                   "Kura Kura", "KuraKuraAlbumCover.jpg")  # KURA-KURA
    data += BTRView.getWikiContent("#000000", "#FFFFFF",
                                   "BETTER", "BETTERAlbumCover.jpg")  # BETTER
    data += FFRView.getWikiContent("#000000", "#FFFFFF",
                                   "FanFare", "FanFareAlbumCover.jpg")  # FANFARE
    data += FNTView.getWikiContent("#000000", "#FFFFFF",
                                   "Fake & True", "FakeNTrueAlbumCover.jpg")  # Fake and True
    data += BRTView.getWikiContent("#000000", "#FFFFFF", "Breakthrough",
                                   "BreakthroughAlbumCover.jpg")  # Breakthrough
    data += HPHPView.getWikiContent("#000000", "#FFFFFF",
                                    "HAPPY HAPPY", "HAPPYHAPPYAlbumCover.jpg")  # HAPPY HAPPY
    data += IWBView.getWikiContent("#000000", "#FFFFFF", "I WANT YOU BACK",
                                   "IWANTYOUBACKAlbumCover.jpg")  # I WANT YOU BACK
    data += SBSView.getWikiContent("#000000", "#ffffff", "STAY BY MY SIDE",
                                   "STAYBYMYALBUMCOVER.jpg")  # Stay by my side
    data += BDZView.getWikiContent("#000000",
                                   "#FFFFFF", "BDZ", "BDZAlbumCover.jpg")  # BDZ
    data += WMUView.getWikiContent("#000000", "#FFFFFF",
                                   "Wake Me Up", "WakeMeUpAlbumCover.jpg")  # Wake Me Up
    data += CDPView.getWikiContent("#000000", "#FFFFFF",
                                   "Candy Pop", "CandyPopAlbumCover.jpg")  # Candy Pop
    data += OMTView.getWikiContent("#000000", "#FFFFFF", "One More Time",
                                   "OneMoreTimeAlbumCover.jpg")  # One More Time

    data += """
----
{{{+1 '''English Albums'''}}}

"""
    data += TFSView.getWikiContent("#ff669e", "#fee6f2",
                                   "The Feels", "TheFeelsAlbumCover.jpeg")  # The feels

    #################
    # Update Database
    print("update database")
    FOLView.updateDatabase()
    TORView.updateDatabase()
    ICSView.updateDatabase()
    MNMView.updateDatabase()
    FSView.updateDatabase()
    FCView.updateDatabase()
    OJJView.updateDatabase()
    YOYView.updateDatabase()
    DNView.updateDatabase()
    WILView.updateDatabase()
    MNHView.updateDatabase()
    HSView.updateDatabase()
    LKYView.updateDatabase()
    TWSView.updateDatabase()
    SGNView.updateDatabase()
    KNKNView.updateDatabase()
    TTView.updateDatabase()
    CHEView.updateDatabase()
    OOHView.updateDatabase()

    # 일본앨범
    DGHView.updateDatabase()
    KURView.updateDatabase()
    PFWView.updateDatabase()
    BTRView.updateDatabase()
    FFRView.updateDatabase()
    FNTView.updateDatabase()
    BRTView.updateDatabase()
    HPHPView.updateDatabase()
    BDZView.updateDatabase()
    IWBView.updateDatabase()
    WMUView.updateDatabase()
    CDPView.updateDatabase()
    OMTView.updateDatabase()
    SBSView.updateDatabase()

    # 영어
    TFSView.updateDatabase()
    print("ok")
    return data
