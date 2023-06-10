# notion-clear-trash

A small script to clear the trash from Notion

### How to Run the Script

1. Clone the repository
```bash
git clone https://github.com/zhousanfu/notion-clear-trash.git
```
2. Install requirements
```bash
# 安装依赖
pip3 install -r requirements.txt
```
3. Run python script
```bash
python3 notion-clear-trash.py
# 执行在终端输入 token_v2
```

### How to Retrieve the Auth Token (in Chrome)
浏览器打开notion 开发者模式F12 Cookie里有'token_v2'
1. Go to notion.so
2. Open developer tools (hit F12)
3. Navigate to the Application tab (may be hidden if the developer window is small)
4. Expand Cookies under the Storage section on the sidebar
5. Click on 'https://www.notion.so' to view all the cookies
6. Copy the value for the key 'token_v2'

![在这里插入图片描述](https://img-blog.csdnimg.cn/5ae4de740d8d4d30bf127ac7c91ae8f4.png#pic_center)