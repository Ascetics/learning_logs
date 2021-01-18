from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.contrib.auth.decorators import login_required

from learning_logs.models import Topic, Entry
from learning_logs.forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """Learning Log"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """显示用户拥有的所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示一个主题及其条目"""
    try:
        topic = Topic.objects.get(id=topic_id)
        if not check_topic_owner(topic, request):
            raise Http404
    except ObjectDoesNotExist:
        raise Http404
    else:
        entries = topic.entry_set.order_by('date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 空白表单
        form = TopicForm()
    else:
        # POST方法提交表单
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """对特定主题添加条目"""
    try:
        topic = Topic.objects.get(id=topic_id)
        if not check_topic_owner(topic, request):
            raise Http404
    except ObjectDoesNotExist:
        raise Http404
    else:
        if request.method != 'POST':
            # 空白表单
            form = EntryForm()
        else:
            # POST方法提交表单
            form = EntryForm(data=request.POST)
            if form.is_valid():
                new_entry = form.save(commit=False)
                new_entry.topic = topic
                new_entry.save()
                return redirect('learning_logs:topic', topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑条目"""
    try:
        entry = Entry.objects.get(id=entry_id)
        topic = entry.topic
        if not check_topic_owner(topic, request):
            raise Http404
    except ObjectDoesNotExist:
        raise Http404
    else:        
        if request.method != 'POST':
            # 用被编辑条目实例化的表单
            form = EntryForm(instance=entry)
        else:
            # POST方法提交的用被编辑条目实例化的表单，数据为提交的数据
            form = EntryForm(data=request.POST, instance=entry)
            if form.is_valid():
                form.save()
                return redirect('learning_logs:topic', topic.id)
    context = {'topic': topic, 'entry': entry, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(topic, request):
    """检查主题用户是否为请求用户"""
    return topic.owner == request.user