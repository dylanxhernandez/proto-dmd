from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import MarkdownContent
from .forms import MarkdownForm

def index_view(request):
    markdown_records = MarkdownContent.objects.order_by('-id')[:10]
    context = {
            'content': {
                'title': 'Home',
                'markdown_list': markdown_records
                }
            }
    return render(
            request,
            'proto_dmd_app/index.html',
            context=context
            )

def redirect_index_view(request):
    return redirect('/')

def markdown_content_view(request, slug):
    markdown_content = get_object_or_404(MarkdownContent, slug=slug)
    context = {'markdown_content': markdown_content}
    return render(
            request,
            'proto_dmd_app/markdown_content.html',
            context=context
            )

def markdown_create(request):
    if request.method == 'POST':
        form = MarkdownForm(request.POST)
        if form.is_valid():
            form.save()    
            return redirect('/')
        else:
            context = {
                    'form': form,
                    'operation': 'Create'
                    }
            response = render(
                    request, 
                    'proto_dmd_app/markdown_form.html', 
                    context=context
                    ) 
            response.status_code = 400
            return response
    else:
        form = MarkdownForm
        context = {
                'form': form,
                'operation': 'Create'
                }
        return render(
                request,
                'proto_dmd_app/markdown_form.html',
                context=context
                )

def markdown_edit(request, id):
    edit_markdown_content = get_object_or_404(MarkdownContent, pk=id)
    if request.method == 'POST':
        form = MarkdownForm(request.POST, instance=edit_markdown_content)
        if form.is_valid():
            form.save()    
            return redirect('/')
        else:
            context = {
                    'form': form,
                    'operation': 'Edit'
                    }
            response = render(
                    request, 
                    'proto_dmd_app/markdown_form.html', 
                    context=context
                    ) 
            response.status_code = 400
            return response
    else:
        form = MarkdownForm(instance=edit_markdown_content)
        context = {
                'form': form,
                'operation': 'Edit'
                }
        return render(
                request,
                'proto_dmd_app/markdown_form.html',
                context=context
                )

