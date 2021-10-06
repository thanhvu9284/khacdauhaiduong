from django.db.models.query_utils import Q
from django.shortcuts import render
from sanpham.models import SanPham,NhomSanPham
from bottom.models import cl_bottom,cl_baohanh_doitra,cl_chinhsach_banhang,cl_chinhsach_giaohang,cl_quydinh_thanhtoan,cl_huongdanmuahang,cl_quychehoatdong,cl_tuyendung
from home.models import homeHotline
from dichvu.models import NhomDichVu

def indexbase(request):
    h_hotline = homeHotline.objects.all()
    sp_noibat =  SanPham.objects.filter(sp_noibat=True)[:6]
    sp_moi =  SanPham.objects.filter(sp_moi=True)[:6]
    sp_khuyenmai =  SanPham.objects.filter(sp_khuyenmai=True)[:6]
    bottom = cl_bottom.objects.all()
    menu_service = NhomDichVu.objects.all().order_by("name")
    menu_sanpham = NhomSanPham.objects.all().order_by("name")
    
    sp_noibat_left =  SanPham.objects.all()[:5]
    sp_moi_left =  SanPham.objects.filter(sp_moi=True)[:5]
    sp_khuyenmai_left =  SanPham.objects.filter(sp_khuyenmai=True)[:5]
    
    data_baohanh = cl_baohanh_doitra.objects.all()
    data_chinhsachbaohanh = cl_chinhsach_banhang.objects.all()
    data_chinhsachgiaohang = cl_chinhsach_giaohang.objects.all()
    data_quydinhhinhthucthanhtoan = cl_quydinh_thanhtoan.objects.all()
    
    data_huongdanmuahang = cl_huongdanmuahang.objects.all()
    data_quychehoatdong = cl_quychehoatdong.objects.all()
    data_tuyendung = cl_tuyendung.objects.all()
    
    context = {
        'menu_service':menu_service,
        'menu_sanpham':menu_sanpham,
        'h_hotline':h_hotline,
        'sp_noibat':sp_noibat,
        'sp_moi':sp_moi,
        'sp_khuyenmai':sp_khuyenmai,
        'bottom':bottom,
        'sp_noibat_left':sp_noibat_left,
        'sp_moi_left':sp_moi_left,
        'sp_khuyenmai_left':sp_khuyenmai_left,
        'data_baohanh':data_baohanh,
        'data_chinhsachbaohanh':data_chinhsachbaohanh,
        'data_chinhsachgiaohang':data_chinhsachgiaohang,
        'data_quydinhhinhthucthanhtoan':data_quydinhhinhthucthanhtoan,
        'data_huongdanmuahang':data_huongdanmuahang,
        'data_quychehoatdong':data_quychehoatdong,
        'data_tuyendung':data_tuyendung
    }
    
    return  context

class SearchResultsView():
    model = SanPham
    template_name = 'searchresult.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = SanPham.objects.filter(
            Q(tieude__icontains=query) | Q(mota__icontains=query) | Q(noidung__icontains=query)
        )
        return object_list