import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
import requests as req
##from bs4 import BeautifulSoup
st.set_page_config(page_title='大开砚界·砚文化与乡村旅游的美丽邂逅', 
                   page_icon='https://i.postimg.cc/GhJyQvHt/1.png',
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   menu_items=None
                  )
cola,colb,colc=st.columns(3)
with cola:
    st.image('https://i.postimg.cc/jj6PjTs5/3.png',width=100)
with colb:
    st.header('')
    st.subheader(':violet[——砚文化与乡村旅游的美丽邂逅]')
with colc:
    st.write('')
st.title(':blue[大开砚界]')
top=st.sidebar.image('https://i.postimg.cc/GhJyQvHt/1.png',width=50)
add_selectbox=st.sidebar.radio(
    ':orange[请选择您想查看的内容]',
    ('大开砚界·主页','大开砚界·历史','砚台·四大名砚','砚台·定制专属美砚','产品售卖','预定服务','专业手艺人')
)
img=st.sidebar.image('https://img1.baidu.com/it/u=4268152884,478670022&fm=253&fmt=auto&app=138&f=JPEG?w=441&h=118')
st.sidebar.write(':blue[在此感谢洛阳市旅游局的合作]')
st.sidebar.image('https://tse1-mm.cn.bing.net/th/id/OIP-C.Y4UVjwiSwIuYja5YZuDctwEmDU?w=250&h=180&c=7&r=0&o=5&dpr=2&pid=1.7',width=150)
if add_selectbox=='大开砚界·历史':
    st.title('大开砚界·历史')
    st.caption('该APP由 :violet[大开砚界]制作')
    st.image('https://www.zhongguofeng.com/uploads/allimg/170216/4-1F216114528.jpg',caption='大开砚界')
    st.write('砚是磨墨的工具，是文房四宝之一，对中国文化的发展，起过重要的作用')
    st.write('这个人类文明相伴物品，大多本身就是一件艺术品，自古都为人们所喜爱。由于它质地坚实，能传百代，也常为收藏家们所收藏')
    st.subheader(':red[砚台雄史]')
    add_choice=st.selectbox(
        ':green[请选择想查看的历史时期]',
        ('两汉','魏晋南北朝','隋唐&五代','宋辽金元','明清','民国至今'))
    if add_choice=='两汉':
        with st.container():
            st.write(':red[1975年湖北凤凰山168号西汉墓出土的一套文具（包括笔、墨、石砚和砚杵、无字木牍和铜削刀），说明书写墨砚，在2000多年前已经形成。]')
            st.subheader(':blue[汉代砚特点]')
            st.write('早期汉砚的形状，多为平素自然石块，中期为圆饼或长方平板。长方平板研出的颜料，不但可供书画之用，也可供人们化妆之用，这种砚亦称黛板。')
            st.write("晚期的在质量、造型和装饰上都发生了变化，质地有石、陶、漆、铜。有的有盖有腿，腿大多三只。有方形腿，圆柱腿。在盖和腿上有龙、狮、猴、鸟和人物图饰。漆砚上有不同颜料，绘制人物和动物图案。铜砚上镶嵌玉和宝石。")
            st.image('https://img1.artron.net/auction/2012/art001582/d/art0015821244.jpg',width=400,caption='汉代美砚')
    elif add_choice=='魏晋南北朝':
        with st.container():
            st.write(':red[自从汉代佛教输入我国之后，外来艺术的影响已有迹可寻。佛教文化与中国文化混交在一起，到南北朝时期更加明显。可以说是艺术史上最辉煌的时代。这从佛教造像艺术和砚的饰纹上便可以找到例证。]')
            st.subheader(':blue[魏晋时期砚的特点]')
            st.write('这一时期的砚，盛行圆盘三足式，长方形四足式，四方形四足式，和带有时代烙印特殊的形式等。材料大多取自各地山上的石炭岩、叶岩、石英石和青石。')
            st.image('https://p1.ssl.qhmsg.com/t01e8dd1656b5e929f1.jpg',width=200,caption='魏晋美砚')
    elif add_choice=='隋唐&五代':
        with st.container():
            st.write(':red[继承南北朝信佛的传统，修建庙宇铸刻佛像，达到了空前的地步。在隋代短短的29年，产生了不少艺术精品。这一时期著名的书画家有智永和展子虔。]')
            st.subheader(':blue[]')
            st.write('在唐代名砚的发现与砚的制作也出现了高峰。像产于广东肇庆的端石砚，产于安徽歙州的龙尾石砚，产于山东青州的红丝石砚和产于山西绛县、河南灵宝的澄泥砚，都是在这一时期相继问世。由于砚在质地上的改观，名砚的尊贵地位，到这时才真正确立。')
            st.image('https://www.zhongguofeng.com/uploads/allimg/170216/4-1F216105542.jpg',width=500,caption='河南洛阳澄泥砚')
    elif add_choice=='宋辽金元':
        with st.container():
            st.write(':red[宋太祖赵匡胤统一中国后，虽后来兵弱屡遭外辱，但文艺方面，像建立书画院、研究院，奖励艺术家，成绩却非常可观。]')
            st.subheader(':blue[宋辽金元时期砚特点]')
            st.write('宋代石砚成了主流，在造型装饰方面，也日臻精美。形制也更加多彩，有风字、四直、箕形、斧形、马蹄、日月形、琴形、石渠、太师等几十个品种。雕刻主体部分一般采取深刀，适当穿插浅刀，有时加以细刻点缀。刻工风格浑厚，显得大方、古朴、雅致。')
            st.image('https://img1.artron.net/auction/2018/art007773/d/art0077733397.jpg',caption='宋犖款端石海水龙纹砚')
    elif add_choice=='明清':
        with st.container():
            st.write(':red[明代是砚成为工艺品的重要历史阶段，由于社会上赏砚及藏砚之风盛行，砚工为了迎合文人雅士的口味，在形式和雕刻上，都超过了前代。]')
            st.subheader(':blue[明清砚特点]')
            st.write('玩赏砚开始成为风尚。特别明万历二十八年，老坑开出了大西洞优质石料，出现了只作欣赏不作使用的平板砚。此外用银、铁、铜、翠玉、水晶等材料作的本不能研墨的砚，在社会上也常见到。')
            st.image('https://ts1.cn.mm.bing.net/th/id/R-C.2cf5f4fee1c7b0610d2eebf30e350b28?rik=FWOko1KVsDKCgA&riu=http%3a%2f%2fwww.xlysauc.com%2fimg%2f2017cp%2fzj%2fd%2f1622.jpg&ehk=Ewfkgi11OfRWj1yGZCMAXWjBYMKC%2bilQf2JgOQW5ru8%3d&risl=&pid=ImgRaw&r=0',caption='海天旭日端砚')
    elif add_choice=='民国至今':
        with st.container():
            st.write(':red[借着清代玩砚高潮的余温，清末民初也出现了一些玩砚的大家。像曾任民国总统的徐世昌和其胞弟徐世章，吴昌硕为其作铭刻铭的沈石友，以及邹鲁、冯恕等。民国年间由于战乱频仍，社会动荡，不少名砚流到了域外，特别是1949年，蒋家王朝撤离大陆，把一些国家收藏的古砚运到了台湾，新中国成立后百废俱兴，各大博物馆重整旗鼓，广泛征集，大批古砚收入到国家藏馆。各地名砚名坑，也重新开掘，恢复了生产。改革开放之后，政治稳定，市场活跃，不管古砚和新砚，玩的人多了起来，又掀起了一股新的玩砚热潮。]')
            st.subheader(':blue[民国至今砚特点]')
            st.write('山西新绛的澄泥砚、吉林长春的松花石砚、河北易县的易水砚、河南南阳的方城石砚、山东青州、临朐的红丝石砚，由于当地政府的重视支持，发展迅速，成效显著。2010年，中国人民武装警察原副司令员刘红军，在上海世博会上展览了他的藏品，举办了中国砚文化高峰论坛，今年又成立了中国砚文化发展委员会，10月还将在北京举办中国砚文化展览，无疑对中国砚文化发展将起到轰动效应。')
            st.image('https://n.sinaimg.cn/sinakd10117/65/w773h892/20200805/dddc-ixkvvuc2604806.jpg',caption='民国之砚',width=400)
    with st.expander('更多信息'):
        st.write(':orange[如果想了解更多关于砚历史的信息，请前往]')
        st.write('http://www.duanyan.cn/index/science/show/1310.html')
        st.image('https://ts1.cn.mm.bing.net/th/id/R-C.9370e9ce822362d27ee0e2712ed2be1b?rik=aXKSD%2blVI%2fibKw&riu=http%3a%2f%2fres.jnnews.tv%2fa%2f10001%2f201802%2f5a640d1c8578ca8b1f99848746c212ef.jpeg&ehk=wdBQi8l6CrCXm7vLdHvAQtJSr1YhpJz65C2m%2fAPCZYs%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1',width=300)   
    st.snow()
elif add_selectbox=='砚台·四大名砚':
    st.header(':orange[四大名砚]')
    st.caption('该APP由 :violet[大开砚界]制作')
    with st.container():
        st.write('砚是一种久负盛名的中国传统手工艺品')
        st.write('中国四大名砚是指甘肃洮州的洮河砚、广东肇庆市的端砚、安徽歙县的歙砚、河南的澄泥砚，它们是中国传统的四大优质名砚')
        st.write('也有人主张，以天然优等紫翠石雕制的易水砚代替澄泥砚，以及山东青州的红丝砚合称四大名砚')
        st.write('砚是中国书法的必备用具。砚台不仅是文房用具，由于其性质坚固，传百世而不朽，又被历代文人作为珍玩藏品之选')
        add_box2=st.selectbox(
            ':violet[请选择想了解的名砚]',
            ('河南澄泥砚','甘肃洮河砚','广东端砚','安徽歙砚'))
        if add_box2=='河南澄泥砚':
            with st.container():
                st.subheader(':blue[河南澄泥砚]')
                st.write('澄泥砚用特种胶泥加工烧制而成因烧过程及时间不同，可以是多种颜色，有的一砚多色，尤其讲究雕刻技术，有浮雕、半起胎、立体、过通等品种。澄泥砚由于使用经过澄洗的细泥作为原料加工烧制而成，因此澄泥砚质地细腻，犹如婴儿皮肤一般，而且具有贮水不涸，历寒不冰，发墨而不损毫，滋润胜水可与石质佳砚相媲美的特点，因此前人多有赞誉。今日所见古澄泥砚极为稀少，上品更是难求。')
                st.image('https://img1.artron.net/auction/2012/art502523/d/art5025230876.jpg',caption='河南澄泥砚')
        elif add_box2=='甘肃洮河砚':
            with st.container():
                st.subheader(':blue[甘肃洮河砚]')
                st.write('洮砚石产于中国甘肃省甘南藏族自治州卓尼县洮砚乡洮河之滨，是水成岩的一种，又名辉绿岩。洮河砚，以其细密晶莹、清丽动人、石纹如丝，似浪滚云涌等特点，为历代皇家所珍藏，备受文人雅士青睐。')
                st.image('https://www.zhongguofeng.com/uploads/allimg/yuansu/37/cduqju1lkki.jpg',caption='甘肃洮河砚')
        elif add_box2=='广东端砚':
            with st.container():
                st.subheader(':blue[广东端砚]')
                st.write('端砚以石质坚实、润滑、细腻、娇嫩而驰名于世，用端砚研墨不滞，发墨快，研出之墨汁细滑，书写流畅不损毫，字迹颜色经久不变，端砚若佳，无论是酷暑还是严冬，用手按其砚心，砚心湛蓝墨绿，水气久久不干，故古人有“呵气研墨”之说。')
                st.image('https://ts1.cn.mm.bing.net/th/id/R-C.01aecedf5df85da032e94ba1fd24bdd7?rik=fuztFN2VXQGfGA&riu=http%3a%2f%2fwww.xlysauc.com%2fimg%2f2020cp%2fyt%2fd%2f3590.jpg&ehk=uNOWskX9m98T6C1x6dYk55CrImZzzWaTQFANFAld85Q%3d&risl=&pid=ImgRaw&r=0')
        elif add_box2=='安徽歙砚':
            with st.container():
                st.subheader(':blue[安徽歙砚]')
                st.write('歙砚为历代文人所称道。南唐后主李煜说“歙砚甲天下”；苏东坡评其“涩不留笔，滑不拒墨，瓜肤而縠理，金声而玉德”；米芾说：“金星宋砚，其质坚丽，呵气生云，贮水不涸”。2004年9月中国轻工联合会和中国文房四宝协会授予歙县“中国歙砚之乡”荣誉称号。')
                st.image('https://img.alicdn.com/bao/uploaded/i4/O1CN01Ht7qkO1OEHCsddWtw_!!0-paimai.jpg')
        with st.expander('[更多详情]'):
            st.write(':orange[如果想了解更多关于四大名砚的信息，请前往]')
            st.write('https://baike.baidu.com/item/%E5%9B%9B%E5%A4%A7%E5%90%8D%E7%A0%9A/4467114')
            st.image('https://cdn.pixabay.com/photo/2020/03/19/08/43/ink-stone-4946771_1280.jpg',width=200,caption=':墨石')
        st.header(':orange[快去定制你的专属砚台吧！]')
    st.balloons()
elif add_selectbox=='砚台·定制专属美砚':
    st.caption('该APP由 :violet[大开砚界]制作')
    st.balloons()
    st.header(':violet[开始定制你的专属美砚!]')
    st.subheader(':blue[了解定制]')
    st.write(':red[一、仅此一砚]')
    st.write('我们希望您用身份文件定制购买,以示您对其的喜爱!')
    col3,col4=st.columns(2)
    with col4:
        st.image('https://i.postimg.cc/c18hXN4k/1672843243009.png',width=300)
    with col3:
        st.image('https://ts1.cn.mm.bing.net/th/id/R-C.2437f383b198a65d595b682091bd6987?rik=%2fUfIGCqSI%2bWhXA&riu=http%3a%2f%2fwww.xlysauc.com%2fimg%2f2011qp%2fyt%2fd%2f884.jpg&ehk=cNGbumoaAoJeeG1pJkLgMufD8%2brer3CVFBj8GkgBUmA%3d&risl=&pid=ImgRaw&r=0')
    st.write(':red[二、个性化定制]')
    st.image('https://ts1.cn.mm.bing.net/th/id/R-C.3c9ba766342aadba8278bc0b358bb40c?rik=9ET6rNzg%2fGUPzQ&riu=http%3a%2f%2fwww.jsdaima.com%2fkindeditor%2fattached%2fimage%2f20171011%2f20171011154047_73241.jpg&ehk=0ADzruj8bkmtzU3b3A1mbmUVpqivi9TzUpDwp5dCTMY%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1')
    st.write('您将在定制面板内看到各种需求，应有尽有')
    st.write(':red[三、入"洞"相看两不厌]')
    st.write('希望您通过此了解河南及三门峡文化')
    col1,col2=st.columns(2)
    with col1:
        st.header(':blue[豫文化]')
        st.image('https://ts1.cn.mm.bing.net/th/id/R-C.61b7787ef782b4c877f9d806dede7a1e?rik=xcEv4T22EQqkbw&riu=http%3a%2f%2fres.1xianxian.cn%2fupload_217a0f46847f032bd2671f92e99118d7.jpg%3fimageView2%2f0%2fw%2f847%2fh%2f640&ehk=cCO0stYGNQPtYJLeRL7ynVN5PF2eLQikGpOSP6EDcCY%3d&risl=&pid=ImgRaw&r=0')
    with col2:
        st.header(':blue[三门峡地坑院]')
        st.image('https://youimg1.c-ctrip.com/target/100210000000od0b791B0.jpg')
    st.header(':violet[现在我们开始定制砚台！]')
    with st.container():
        add_boxr=st.radio(':blue[请选择你喜欢的砚台颜色]',['红色','黄色','绿色','黑色','蓝色','其他'])
        if add_boxr=='其他':
            颜色=st.text_input(':orange[请输入你心仪的砚台颜色]','紫色')
        add_boxr2=st.radio(':blue[请选择你心仪砚的质地]',['质地较硬','质地均匀','质地较软','其他'])
        if add_boxr2=='其他':
            质地=st.text_input(':orange[请输入您心仪的砚台质地]','均可')
        add_boxr3=st.radio(':blue[请选择您是否希望您的砚台有浮雕]',['是','否'])
        if add_boxr3=='是':
            浮雕=st.text_input(':orange[请输入您希望砚台的浮雕类型]','荷花')
        add_boxr4=st.radio(':blue[请选择您是否希望您的砚台有诗文雕刻]',['是','否'])
        if add_boxr4=='是':
            add_boxr5=st.multiselect(':blue[请选择您想刻的诗文(可多选)]',['虞美人','长相思','青玉案'])
            st.caption(':green[暂时只支持此三首]')
        text=st.text_area(':blue[请备注其他请求]')
        text2=st.text_input('请填写您的住址')
        add_boxr7=st.selectbox(':blue[请选择身份文件](选填)',['身份证','其他'])
        text3=st.text_input(':orange[请输入身份信息]','选填')
        add_boxr6=st.radio('请问您是否定制好了心仪的砚台',['否','是'])
        if add_boxr6=='是':
            st.success('恭喜您定制完毕,美砚将马上到您文案桌上')
            st.subheader(':blue[请在此跳转付款页]')
            st.write('https://qr.alipay.com/fkx18818z6dc3sjyyxbgw1c')
            st.balloons()
elif add_selectbox=='大开砚界·主页':
    tab1,tab2,tab3,tab4=st.tabs(['首页','咨询','创意','产品'])
    with tab1:
        st.image('https://i.postimg.cc/8P0HYp72/1673017894520.png',width=300)
        st.write('大开砚界项目是一个面向澄泥文化与乡村旅游的特色三农项目，是一个系统化、人性化、中国优秀历史文化的传承性、且具有穿心盈利模式的澄泥文化特色乡村旅游项目。我们将依托当地的历史文化，结合乡村旅游的形式，以电子商务为运营模式，以互联网为平台，致力于带动新冠疫情后非遗文化传承与乡村旅游恢复发展。我们将把澄泥砚文化融入到乡村旅游之中，通过不断创新产品来吸引游客，借此来推动三农工作的实施。该项目具有较强的专门性、文化性、中国特色性和时代性，活力较大，未来可期。')
        st.write(':blue[您将在这里体验到砚文化乡村旅游服务,包括相关产品、预定服务和专业手艺人服务]')
    with tab2:
        st.image('https://i.postimg.cc/GhJyQvHt/1.png')
        st.write(':blue[如果您想加入我们,请联系我们的邮箱或电话]')
        st.write(':postbox: 3143690898@qq.com')
        st.write(':phone: 17624890380')
    with tab3:
        st.image('https://i.postimg.cc/VfLhnh1N/20230318205728.png?dl=1',width=300)
        st.write(':blue[本公司采用了以互联网为平台，以澄泥砚文化与乡村旅游为核心，以创新产品及服务为创意，致力于三农战略的实施]')
    with tab4:
        st.header(':blue[产品示例]')
        st.subheader('犀纹宝瓶砚')
        st.image('https://i.postimg.cc/YSnf7bvr/1.png')
        st.write('此砚由制砚大师惠东存先生仿宋德寿殿犀纹亲手制作而成')
        st.write('通体澄泥质，色泽灰褐，沉静凝重，直角长方形，正面琢出瓶形砚堂')
        st.write('造型严整，雕琢有致，无过多纹饰，简约大方')
        st.write('以瓶口为墨池，瓶身为受墨处，瓶身砚面刻犀纹，每一处的细节都堪称艺术品')
        st.write('自古以来,国人都用 "瓶"寓意平安,这样一款古意满满的瓶形砚堂,不仅能满足书画要求,也满载对美好生活的祝福之情')
if add_selectbox== '产品售卖':
    st.title(':red[大开砚界——产品售卖]')
    choice=st.selectbox(
        ':green[请选择想查看的产品]',
        ('日常类','文创类'))
    if choice=='日常类':
        st.subheader(':blue[与砚文化结合的特色作品]')
        product=st.selectbox('请选择想查看的特色产品',['澄泥 十二生肖彩绘摆件','澄泥 乡村娃娃','澄泥 迷你花瓶','澄泥 笔筒','澄泥 茶宠','澄泥 烛台'])
        if product=='澄泥 十二生肖彩绘摆件':
            st.image('https://i.postimg.cc/MKzV7qSM/1.png')
            st.write(':blue[原料：澄泥]')
            st.write(':blue[做法：手工捏制]')
            st.write(':blue[产地：三门峡]')
            st.write(':blue[特色：可爱萌趣，手工彩绘，磨砂质感]')
            st.radio('是否加入购物车',['否','是'])
        elif product=='澄泥 乡村娃娃':
            st.image('https://i.postimg.cc/qMmh2KwS/2.png')
            st.write(':blue[原料：澄泥]')
            st.write(':blue[做法：手工捏制]')
            st.write(':blue[产地：三门峡]')
            st.write(':blue[特色：高温烧制，防水防高温，可爱卡通，生动形象]')
            st.radio('是否加入购物车',['否','是'])
        elif product=='澄泥 迷你花瓶':
            st.image('https://i.postimg.cc/Y0TcwbkT/3.png')
            st.write(':blue[原料：澄泥]')
            st.write(':blue[做法：手工捏制]')
            st.write(':blue[产地：三门峡]')
            st.write(':blue[特色：手工彩绘，造型美观，小巧精致]')
            st.radio('是否加入购物车',['否','是'])
        elif product=='澄泥 笔筒':
            st.image('https://i.postimg.cc/WbtWGGjJ/4.png')
            st.write(':blue[原料：澄泥]')
            st.write(':blue[做法：手工捏制]')
            st.write(':blue[产地：三门峡]')
            st.write(':blue[特色：小巧可爱，实用型笔筒]')
            st.radio('是否加入购物车',['否','是'])
        elif product=='澄泥 茶宠':
            st.image('https://i.postimg.cc/y84mDcNK/5.png')
            st.write(':blue[原料：澄泥]')
            st.write(':blue[做法：手工捏制]')
            st.write(':blue[产地：三门峡]')
            st.write(':blue[特色：耐高温，耐水性强，卡通设计]')
            st.radio('是否加入购物车',['否','是'])
        elif product=='澄泥 烛台':
            st.image('https://i.postimg.cc/j5mXv9Rw/6.png')
            st.write(':blue[原料：澄泥]')
            st.write(':blue[做法：手工捏制]')
            st.write(':blue[产地：三门峡]')
            st.write(':blue[特色：典雅精致，小巧玲珑]')
            st.radio('是否加入购物车',['否','是'])
    elif choice=='文创类':
        st.subheader(':blue[与砚文化结合的特色文创产品]')
        wen=st.selectbox(
           ':blue[请选择感兴趣的文创产品]',
            ('景点联名砚台','主题故事砚台')
        )
        if wen == '景点联名砚台':
            st.subheader(':blue[大开砚界积极寻求与其他旅游景点相交流互鉴，为此创造出许多颇具创意的产品]')
            st.image('https://i.postimg.cc/FFgt1gpb/20230319080544.jpg')
            st.write(':green[这是我们与洛阳云冈石窟一同做的一步尝试，后续我们也将积极寻求其他合作伙伴]')
            st.radio('是否加入购物车',['否','是'])
        elif wen =='主题故事砚台':
            st.subheader(':blue[赋予其故事的砚台，收藏的底蕴深厚]')
            tab_a,tab_b=st.tabs(['九瓣莲花瓦当砚','大河奔流砚'])
            with tab_a:
                st.image('https://i.postimg.cc/zDLsFYqj/1.png')
                st.caption('九瓣莲花瓦当砚')
                st.write('此砚由制砚大师惠东存先生制作而成')
                st.write('唐朝吴融《古砚瓦赋》中描述： “无谓乎柔而无刚，土埏而为瓦；勿谓乎废而不用，瓦断而为砚')
                st.write('自秦汉起，建筑皇家宫殿、寺庙等古建筑用的砖瓦，饰以文字或者图案，多采用澄泥制法')
                st.write('这个九瓣莲花瓦当砚，就是 依唐代莲花瓦当残片，经古法手工雕刻，还原制作而成')
                st.write('为了与古瓦当的高古远久和谐一致，雕刻时颇费功夫。整体为圆形，九瓣莲花围绕四周，莲心刻字“安”，寓： 外圆内方，人正心安')
                st.radio('是否加入购物车?',['否','是'])
            with tab_b:
                st.image('https://i.postimg.cc/yNNKqfZY/2.png')
                st.caption('大河奔流砚')
                st.write('此砚台由游敏大师制作而成')
                st.write('一方圆润的澄泥砚，周身沁着独有的“鳝鱼黄”，黄白色波纹状窑变仿似奔涌的浪花，“行云流水”间充盈着黄河的神韵')
                st.write('这方名为“大河奔流”的澄泥砚，历经采泥、洗泥、制坯、雕刻和10余天不间断人工焙烧等64道工序，最终完美面世')
                st.write('游敏介绍，澄泥砚是以黄河澄泥为主要材质经焙烧而成的陶质砚，其中含有诸多矿物质，均采集于禹门口至花园口近300公里的黄河岸边')
                st.write('经过多年的测验，目前共挑选出30余处采泥点。“我是长在黄河边的黄河人，用黄河泥来创作澄泥砚，并将博大精深的黄河文化传承出去，是我毕生的目标。”游敏说')
                st.radio('是否加入购物车',['否','是'])
    with st.expander('产品相关——制作详情'):
        st.image('https://x0.ifengimg.com/res/2021/28B65175349BD8D908C63B679BABD3A636DB184D_size645_w823_h770.png')
    st.balloons()
if add_selectbox== '预定服务':
    st.title(':red[大开砚界——预定服务]')
    tab_1,tab_2,tab_3=st.tabs(['门票预定','餐厅预订','民宿预订'])
    with tab_1:
        st.subheader(':blue[特色地坑院预定服务]')
        st.image('https://tse2-mm.cn.bing.net/th/id/OIP-C.KdAHEpm6OpMm1sTkYGQwUwHaEK?w=326&h=183&c=7&r=0&o=5&dpr=2&pid=1.7')
        st.write(':blue[您将在这里体验到结合砚文化的乡村旅游,必定使您“大开砚界”]')
        st.radio('是否需要预定门票？',['否','是'])
        st.caption(':green[您凭借电子门票即可进入游玩]')
    with tab_2:
        st.subheader(':blue[”舌尖砚旅“预定服务]')
        st.image('https://tse2-mm.cn.bing.net/th/id/OIP-C.1BUV6PSmNwQBTHcMSTrXNQHaFj?w=221&h=180&c=7&r=0&o=5&dpr=2&pid=1.7')
        st.write(':blue[”舌尖砚旅“——同当地砚文化相结合的特色食品餐厅]')
        st.radio('是否需要预定“舌尖砚旅”的门票？',['否','是'])
    with tab_3:
        st.subheader(':blue[”民宿之行“预定服务]')
        st.image('https://tse3-mm.cn.bing.net/th/id/OIP-C.N1MyJnqJdBafsbVfdfV7CAHaFj?w=264&h=198&c=7&r=0&o=5&dpr=2&pid=1.7')
        st.write(':blue[“民宿之行”——同当地的居民一起领略砚文化与乡村的魅力]')
        st.radio('是否需要预定“民宿之行”的门票？',['否','是'])
    with st.expander('当地历史及现状'):
        st.image('https://tse4-mm.cn.bing.net/th/id/OIP-C.viYkGk33XFocJqgXQo_TywHaFj?w=249&h=183&c=7&r=0&o=5&dpr=2&pid=1.7')
        st.write(':blue[陕州地坑院，作为一种古老而神奇的民居样式，地坑院蕴藏着丰富的文化，是全国乃至世界唯一的地下古民居建筑，是我国特有的四大古民居建筑之一。被誉为“地平线下古村落，民居史上活化石”]')
        st.write(':blue[景区采取打卡式旅游，每个院落中会展示1-2个不同的澄泥砚制作工序，设置有体验区提升游客体验感，我们为每个院落都设计了一张独有的身份卡，游客再参观完后相关院落即可获得该身份卡，集满15张可以去服务台领取精美礼品一份。]')
    st.balloons()
elif add_selectbox== '专业手艺人':
    st.title(':red[大开砚界——专业手艺人]')
    tab_l,tab_z,tab_h=st.tabs(['蔺永茂','温生康','张慧'])
    with tab_l:
        st.subheader(':red[蔺永茂非遗传承人]')
        st.image('http://www.xinhuanet.com/shuhua/20230217/b3ac8395973e45bdab34aac956f1b7de/20230217b3ac8395973e45bdab34aac956f1b7de_20230217134d5762568142538fe7a444faae9532.jpg')
        st.write(':blue[澄泥砚是中国四大名砚之一，使用经过澄洗的细泥作为原料加工烧制而成，有着质地细腻、抚如童肌、发墨而不损毫等特点，尤以山西绛州澄泥砚为主要代表。其制作技艺曾一度失传，后在山西新绛蔺永茂、蔺涛父子的努力下重现于世。澄泥砚制作需要经过选泥、澄清、阴干、雕刻、打磨、烧制等十余道主要工序，生产周期长达一年左右。2008年，“砚台制作技艺·澄泥砚制作技艺”被列入国家级非物质文化遗产名录]')
    with tab_z:
        st.subheader(':red[温生康大师]')
        st.image('http://p8.itc.cn/images01/20200720/66f06be21567496996709b1c34aa0b12.jpeg')
        st.write(':blue[温氏澄泥空心砚质坚细腻，储墨益毫，温润沉静，制作工艺独特，技术含量高。其代表产品有“八漏七不漏”的古玩产品“观音赐露”，青铜器式顶尖产品“四羊方樽”，还有青铜器式砚、鼎、豆、瓶等系列产品。色泽有青铜色、紫铜色、豆绿色、鳝鱼黄等。系列产品有20多项申请了国家专利]')
    with tab_h:
        st.subheader(':red[张慧非遗传承人]')
        st.image('https://www.workercn.cn/upload/resources/image/2022/10/11/163911.jpg?r=1665454412260')
        st.write(':blue[黄河澄泥砚是中国四大名砚之一，因制作技艺复杂，曾消失数百年。1991年，张慧的父母张存生和王玲历经131次失败恢复了黄河澄泥砚制作工艺。因从小生活在郑州的黄河岸边，跟随父母学习黄河澄泥砚的制作技艺，张慧大学毕业后就开始了黄河澄泥砚的传承]')
        st.write(':red[如今，张慧是河南省非遗项目黄河澄泥砚的第六代传承人]')
    st.balloons()
st.write(':red[Tips]：:green[别忘了左上角的小箭头]:bell:')
col5,col6=st.columns(2)
with col5:
    st.subheader(':blue[关于我们]')
    box=st.selectbox('默认版本',['3.11'])
    box2=st.selectbox('活动',['暂无'])
    st.image('https://i.postimg.cc/jj6PjTs5/3.png',width=100)
with col6:
    st.subheader(':blue[联系我们]')
    st.write('官方网站:https://www.lntu.edu.cn/')
    st.write(':telephone_receiver:  0418-5110337')
    st.write(':email: xcb@lntu.edu.cn')
    st.write(':office: 葫芦岛市兴城市龙湾南大街188号辽宁工程技术大学')
    st.image('https://img1.baidu.com/it/u=4268152884,478670022&fm=253&fmt=auto&app=138&f=JPEG?w=441&h=118')

                
            
    
    
    



