<template>
    <div :id="id" style="height: 100%; weight: 100%;">
        <el-row justify="end" style="margin-left: 64.8%; margin-bottom: 1%;">
            <el-button info>
                <el-icon class="el-icon--left">
                    <Back />
                </el-icon>Reset Data or Chart Type
            </el-button>
            <el-button plain>
                Delete<el-icon class="el-icon--right">
                    <Delete />
                </el-icon>
            </el-button>
        </el-row>
    </div>
</template>

<script>
import { ElRow, ElCol, ElButton, ElIcon, ElPopover, ElCheckbox } from 'element-plus'
let vm = null;
import { render, ref } from 'vue'
import {
    Delete,
    Back,
} from '@element-plus/icons-vue'

export default {
    name: "CharCellToolbar",
    components: {
        ElButton,
        ElIcon,
        Delete,
        Back,
    },
    props: {

    },
    data() {
        return {
            id: "chart-cell-toolbar-" + "aaa",
        }
    },
    mounted() {

    }

}
</script>