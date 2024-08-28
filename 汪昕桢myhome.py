#记得改文件名
'''我的主页'''
import streamlit as st
from PIL import Image
import time
import base64
pip install streamlit
streamlit hello



def bar_bg(img):
    last = 'png'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'png'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('汪侧边栏.png')
page_bg('汪bg.png')
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区','美食推荐'])

def page_1():
    '''我的兴趣推荐'''
    st.title('兴趣推荐')
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    st.write(':blue[我喜欢弹琴画画玩魔方打乒乓球......我还是一名“吃货”]')
    st.image('汪1.png')
    st.image('汪2.png')
    st.image('汪3.png')
    st.write(':blue[我是重庆人，我们这里有热门景点，例如洪崖洞、解放碑]')
    st.image('汪19.png')
    st.image('汪20.png')
    st.write(':blue[也有数不胜数的美食（重庆小面、火锅、糍粑.....）]')
    st.image('汪21.png')
    st.image('汪22.png')
    st.markdown(':rainbow[该网站不仅推荐美食，还配备图片处理、智能词典、留言区，希望你能有更好的体验]')
    
    
def page_2():
    '''我的图片处理工具'''
    st.title('图片处理工具')
    st.subheader(':blue[:heart_eyes:图片换色工具:heart_eyes::smirk::smirk:]')
    st.write(':blue[:heart_eyes:改色后的图片可以点下载按钮下载，大胆的改色吧:heart_eyes::smirk::smirk:]')
    st.write(':green[:heart_eyes:教程如下:heart_eyes::smirk::smirk:]')
    st.video('汪图.mp4')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5 = st.tabs(["原图","改色1","改色2","改色3","改色4"])
        with tab1:
            st.image(img)
            st.write(':blue[:heart_eyes:谢谢你的图片:heart_eyes::smirk::smirk:]')
            #img.save(f'{file_name}_备份.png')
        with tab2:
            st.image(img_change(img,0,2,1))
            st.write(':blue[:heart_eyes:哇塞:hushed::hushed::wink::smirk:]')
        with tab3:
            st.image(img_change(img,1,2,0))
            st.write(':blue[:hushed:红绿蓝的奇妙搭配:heart_eyes::smirk:]')
        with tab4:
            st.image(img_change(img,2,0,1))
            st.write(':blue[:grin:有趣极了:heart_eyes::heart_eyes:]')
        with tab5:
            st.image(img_change(img,1,0,2))
            st.write(':blue[:heart_eyes:真不错:heart_eyes::smirk::smirk:]')
            st.write(':blue[:heart_eyes:我是不是很厉害:sunglasses::sunglasses::smirk::wink::kissing_heart:]')
        
            
        img.save(file_name)
        with open(file_name,'rb') as file:
            btn=st.download_button(
                label='下载',
                data=file,
                file_name=f'{file_name}_改色后.png',
                mime='image/png'
            )
    
        
   
def page_3():
    '''我的智能词典'''
    st.title('智能词典')
    st.write(':blue[在框框中输入想搜的单词，然后按enter键]')
    st.write(':rainbow[你好呀!我准备了神秘小彩蛋。尝试分别输入network,active,achieve,tasteful（按顺序来）,你会分别得到四个字母，拼起来输入可以找到彩蛋。]')
    with open('汪words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
        
    with open('汪check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n') 
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
        
    word=st.text_input('查个英文单词')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('汪check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            f.write(message)
                
        st.write('查询次数：',times_dict[n])
    
        if word=='nice':
            st.code('''
                    #恭喜你触发神秘彩蛋，这是一段python代码
                    print('Hello')''')
            st.balloons()
            st.balloons()
            st.write(':green[气球飘飘]')
            st.write(':green[你真厉害:sunglasses::sunglasses:]')
            
        elif word=='network':
            st.write('n')
        elif word=='active':
            st.write('i')
        elif word=='achieve':
            st.write('c')
        elif word=='tasteful':
            st.write('e')
        
            
def page_4():
    '''我的留言区'''
    st.title('留言区')
    st.write(' ')
    st.write(':blue[教程如下]')
    st.write(':blue[先输入留言，再按enter键，最后点留言键，即可发送留言]')
    st.video('汪4.mp4')
        
    with open('汪leave_messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('\n') 
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        if i[1]=='阿短':
            with st.chat_message('🌈'):
                st.write(i[1],':',i[2])
        elif i[1]=='编程猫':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1]=='游客1':
            with st.chat_message('🌆'):
                st.text(i[1]+':'+i[2])
        elif i[1]=='游客2':
            with st.chat_message('🌏'):
                st.text(i[1]+':'+i[2])
        elif i[1]=='游客3':
            with st.chat_message('🌟'):
                st.text(i[1]+':'+i[2])
        elif i[1]=='游客4':
            with st.chat_message('🌸'):
                st.text(i[1]+':'+i[2])
        elif i[1]=='游客5':
            with st.chat_message('🏅'):
                st.text(i[1]+':'+i[2])
                
    name = st.selectbox('我是……', ['阿短', '编程猫','游客1','游客2','游客3','游客4','游客5'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])

        with open('汪leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_5():
    '''美食推荐'''
    st.title('美食推荐')
    
    # 滑动条st.slider()
    #cb = st.checkbox('勾选选项')
    #if cb:
        #st.write('选项被勾选', cb)
    
    # 如何创建勾选框？
    # 勾选框更适合单选还是多选？
    # 勾选框的返回值是选框中的字符串吗？不是的话，返回值是什么？
    
    st.write('----')
    st.write(':blue[你喜欢吃什么(可多选)]')
    cb1 = st.checkbox(':blue[健康食品]')
    cb2 = st.checkbox(':blue[垃圾食品]')
    l = [cb1, cb2]
    if st.button('确认答案'):
        if cb1== True:
            st.write(':green[你的饮食习惯很不错]:sunglasses:')
        else:
            st.write(':red[你吃得不太健康]')
        st.subheader(':blue[饿了么]:sunglasses:')
            
        st.image('汪5.png')
        st.image('汪6.png')
        st.image('汪7.png')
        st.image('汪8.png')
        st.image('汪9.png')
        st.image('汪10.png')
        st.image('汪11.png')
        st.image('汪12.png')
        st.image('汪13.png')
        st.image('汪14.png')
        st.image('汪15.png')
        st.image('汪16.png')
        st.image('汪17.png')
        st.image('汪18.png')
        st.header(':blue[做薯条步骤]')
        st.write(' ')
        st.write(':blue[步骤1：把土豆洗净，削皮，切成条状]')
        st.write(':blue[步骤2：将土豆放入锅里，加水，煮熟后捞出]')
        st.write(':blue[步骤3：先开个火，锅里没有水后倒较多的油，导入土豆条，用锅铲翻动土豆条，带所有土豆条均呈金黄色后捞出]')
        st.write(':blue[步骤4：倒入土豆条复炸，锅铲翻动土豆条，土豆条呈焦黄色后捞出]')
        st.header(':rainbow[未完待续]')

        
        
        
        
    
def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

    
if page=='我的兴趣推荐':
    page_1()
elif page=='我的图片处理工具':
    page_2()
elif page=='我的智能词典':
    page_3()
elif page=='我的留言区':
    page_4()
elif page=='美食推荐':
    page_5()

  
    
