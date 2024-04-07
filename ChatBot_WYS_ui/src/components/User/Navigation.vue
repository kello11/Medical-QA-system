<template>
    <div class="navigation">
        <div class="botname">ChatBot_WYS
        </div>
        <div class="tools">
            <el-col :span="12">
                <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
                    background-color="#141718" text-color="white" active-color="#3f494c">
                    <el-menu-item index="1">
                        <i class="el-icon-document"></i>
                        <span slot="title">医疗问答</span>
                    </el-menu-item>
                    <el-menu-item index="2">
                        <i class="el-icon-menu"></i>
                        <span slot="title" @click="showSearchBox">搜索栏</span>

                    </el-menu-item>
                    <el-menu-item index="3">
                        <i class="el-icon-document"></i>
                        <span slot="title">导航三</span>
                    </el-menu-item>
                    <hr>
                    </hr>
                    <el-menu-item index="4">
                        <a :href="'https://www.xywy.com/'" target="_blank" class="plain-link">
                            <i class="el-icon-setting"></i>
                            <span slot="title">权威网站</span>
                        </a>
                    </el-menu-item>
                    <el-menu-item index="5">
                        <i class="el-icon-document"></i>
                        <span slot="title">关于我们</span>
                    </el-menu-item>
                </el-menu>

            </el-col>
        </div>
    </div>
</div></template>

<style>
.plain-link {
    color: inherit;
    text-decoration: none;
}

.plain-link:hover {
    text-decoration: underline;
}

.navigation {
    background-color: #141718;
    height: 820px;
}

.tools {
    position: relative;
    left: 10px;
    top: 100px;

    .el-menu {

        width: 328px;

        .el-menu-item {
            font-size: 20px;
            margin-top: 30px;
        }
    }

}

.search-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.search-input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-right: 8px;
    font-size: 14px;
}

.search-button {
    display: inline-block;
    padding: 8px 16px;
    background-color: #007bff;
    color: #fff;
    border-radius: 4px;
    text-decoration: none;
    font-size: 14px;
}

.botname {
    color: white;
    left: 20px;
    position: absolute;
    /* or absolute */
    top: 20px;
    font-size: 35px;
    font-weight: bold;
}

.search-button:hover {
    background-color: #0056b3;
}
</style>

<script>
import { MessageBox, Message } from 'element-ui';
export default {
    data() {
        return {
            isCollapse: true,
            isSearchVisible: false,
            searchQuery: ''
        };
    },
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        showSearchBox() {
            this.isSearchVisible = true;
        },
        showSearchBox() {
            MessageBox.prompt('请输入内容', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                inputType: 'text'
            })
                .then(({ value }) => {
                    if (value) {
                        const baseUrl = 'https://www.baidu.com/s';
                        const query = { wd: value };
                        const params = new URLSearchParams(query);
                        const url = `${baseUrl}?${params.toString()}`;

                        // 在新标签页中打开搜索结果
                        window.open(url, '_blank');

                        // 处理输入的内容
                        Message.success(`你输入的内容是：${value}`);
                    } else {
                        Message.warning('请输入内容');
                    }
                })
                .catch(() => {
                    Message.info('已取消输入');
                });
        }

    }
}
</script>