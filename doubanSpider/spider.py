from pyReptile import request, dataPattern
from fields import MovieComment, MovieInfo

# Setting parameters
DATABASE_CONNECTION = 'mysql+pymysql://root:1234@localhost/spiderdb?charset=utf8mb4'
movieComment = MovieComment(DATABASE_CONNECTION)
movieInfo = MovieInfo(DATABASE_CONNECTION)


# Movie info
def get_movie(movieId):
    r = request.get(movieUrl % (movieId))
    name = dataPattern.get_data(r['text'], 'h1 > span')[0]
    summary = dataPattern.get_data(r['text'], '#link-report')[0].strip()
    movieDic = dict(movieId=movieId, name=name, summary=summary)
    # Query data
    queryMovie = movieInfo.DBSession.query(movieInfo.table).filter_by(movieId=movieId).all()
    if queryMovie:
        condition = {'movieId': movieId}
        movieInfo.update(movieDic, condition)
    else:
        movieInfo.insert(movieDic)


# Movie Comment
def get_comment(movieId):
    urlList = []
    for page in range(10):
        urlList.append(commentUrl % (movieId, str(page * 20)))
    valueList = []
    responseList = request.get(urlList)
    for response in responseList:
        commentList = dataPattern.get_data(response['text'], 'div.comment > p > span')
        userList = dataPattern.get_data(response['text'], 'span.comment-info > a')
        for comment, user in zip(commentList, userList):
            valueList.append(dict(movieId=movieId, user=user, comment=comment))
    # insert data
    movieComment.insert(valueList)


if __name__ == '__main__':
    # spider
    movieUrl = 'https://movie.douban.com/subject/%s/?from=showing'
    commentUrl = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=20&sort=new_score&status=P'
    movieId = '3168101'
    get_movie(movieId)
    get_comment(movieId)

