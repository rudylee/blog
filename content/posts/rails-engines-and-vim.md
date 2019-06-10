+++
title = "Rails Engines and Vim"
date = "2015-05-03"
slug = "2015/05/03/rails-engines-and-vim"
Categories = ["Ruby on Rails", "Vim"]
+++

At the moment, I am working on a Ruby on Rails projects using Rails Engines ( you can read more about Rails Engines here: [http://guides.rubyonrails.org/engines.html](http://guides.rubyonrails.org/engines.html) ). In this post, I'll share my tips and trick on how to configure your vim to work with Rails Engines.

# NERDTree Bookmark

I am using NERDTree Bookmark to quickly jump between different engines. If you are using NERDTree, you can create a bookmark by putting your cursor on one of the Rails Engines directory and use the command below:

```
:Bookmark <engine name>
```

After you created the bookmark, you can see the bookmarks list by pressing `B` inside NERDTree window. See the screenshot below:

[![](/images/vim-bookmarks.png)](/images/vim-bookmarks.png)

I also added these two options to my vimrc file.

```
" Automatically show bookmarks list when you open NERDTree
let NERDTreeShowBookmarks=1
let NERDTreeChDirMode=2
``` 

`NERDTreeChDirMode` changes the current working directory of your vim to your bookmark directory. This will also enable my favourite rails.vim feature which is open alternate file. 

# CtrlP Working Path Mode

It is normal for Rails Engines to share similar directory structure and filenames. However, this creates problem when you want to search a file using CtrlP plugin. Combined with `NERDTreeChDirMode`, you can tell CtrlP to search only in the current working directory.

Add this option to your vimrc file to enable this feature:

```
let g:ctrlp_working_path_mode = 'a'
```

That's it for now, I'll update this post if I find a better workflow or configuration. If you are interested, you can check my full vimrc file here: [https://github.com/rudylee/dotfiles/blob/master/vimrc](https://github.com/rudylee/dotfiles/blob/master/vimrc)
