from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .models import Post
# Create your views here.
from django.views import View
from .forms import VariableForm
from .myfun import myfun
from .myfun import *




def post_list(request):

        if request.method == "POST":
            form = MyForm(request.POST)

            if form.is_valid():

                x = form.cleaned_data['part_number']
                d2 = form.cleaned_data['today_dollar']
                x = Post.objects.filter(partnumber=x).values()
                for i in x:
                    i['newprice'] = int((int(d2) * int(i['past_price']))/int(i['past_dollar']))
                    i['new_dollar'] = d2
       
            context = {'x': x  }
            return render(request , 'blog/post_result.html' , context )

        if request.method == "GET":
            
            form = MyForm()
            context = {'form': form }
            return render(request, 'blog/post_list.html', context)




class CourseFunc(View):

    def get(self, request):

        form = VariableForm()
        return render(request ,  'data/searchhome.html' , {'form': form})

    def post(self , request):

        form = VariableForm(request.POST)

        if form.is_valid():

            x =form.cleaned_data['X']

            lust = [x]
            myfun(lust , clean )


            context = {'pred': myfun(lust , clean ) }
            return render(request ,  'data/result.html' , context=context )


