# 用这个脚本执行的话 config.js 中的 dest 参数暂时不能设置，之后有空了再来处理这个问题
project_path=$(cd `dirname $0`; pwd) # 文件夹路径
project_name="${project_path##*/}" # 文件夹名称

action=$1
docs_name=$2
repos_dir=repos # project_dir/repos
abs_repos_dir=${project_path}/${repos_dir}
rel_dist_dir='.vuepress/dist' # config.js -> dest

# 如果 repos 文件夹路径不存在则退出
if [ ! -d $abs_repos_dir ]; then
    echo "directory $abs_repos_dir does not exists"
    exit
fi

deploy(){
    # project name
    name=$1
    # docs 和 dist 路径
    docs_abs_path=${abs_repos_dir}/${name}
    dist_path=${abs_repos_dir}/${name}/${rel_dist_dir}
    # git 仓库
    github_repo=https://github.com/xiaminghu/${name}.git
    gitee_repo=https://gitee.com/xiaminghu/${name}.git
    # echo ${dist_path}
    # echo ${github_repo}
    # echo ${gitee_repo}

    # 如果目标 docs 路径不存在，则退出
    if [ ! -d ${docs_abs_path} ]; then
        echo "directory ${docs_abs_path} does not exists"
        exit
    fi



    case $action in
        dev)
            # echo "dev"
            npx vuepress dev ${docs_abs_path}
        ;;
        build)
            # echo "build"
            npx vuepress build ${docs_abs_path}

            # 如果 build 之后 dist 路径不存在，则退出
            if [ ! -d ${dist_path} ]; then
                echo "directory ${dist_path} does not exists"
                exit
            fi
        ;;
        deploy)
            npx gh-pages -d ${dist_path} -r ${gitee_repo}
            npx gh-pages -d ${dist_path} -r ${github_repo}
            python auto-pages.py ${docs_abs_path}
        ;;
        bd)
            ./run.sh build ${docs_name}
            ./run.sh deploy ${docs_name}
        ;;
        *)
            echo "action" $action invalid
    esac


}

deploy ${docs_name}
